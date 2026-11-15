"""Redis-backed rate limiter for multi-instance deployments."""

import time
from typing import Optional

from users.rate_limiting.backend import RateLimiterBackend


class RedisRateLimiter(RateLimiterBackend):
    """
    Redis-backed rate limiter for multi-instance deployments.
    Uses Redis sorted sets to store request timestamps.
    """

    def __init__(self, max_requests: int, window_seconds: int, redis_client):
        """
        Initialize Redis rate limiter.
        
        Args:
            max_requests: Maximum number of requests allowed in the time window
            window_seconds: Time window in seconds
            redis_client: Redis client instance (from redis package)
        """
        super().__init__(max_requests, window_seconds)
        self.redis = redis_client
        self.key_prefix = "rate_limit:"

    def _get_redis_key(self, key: str) -> str:
        """Get the Redis key for a rate limit key."""
        return f"{self.key_prefix}{key}"

    def is_allowed(self, key: str) -> bool:
        """
        Check if a request from the given key is allowed.
        
        Args:
            key: Identifier (IP address or user ID)
            
        Returns:
            True if request is allowed, False if rate limit exceeded
        """
        redis_key = self._get_redis_key(key)
        now = time.time()
        cutoff_time = now - self.window_seconds
        
        # Remove old timestamps outside the window
        self.redis.zremrangebyscore(redis_key, 0, cutoff_time)
        
        # Check if limit exceeded
        count = self.redis.zcard(redis_key)
        if count >= self.max_requests:
            return False
        
        # Record this request as a sorted set score
        self.redis.zadd(redis_key, {str(now): now})
        
        # Set expiration to clean up old keys
        self.redis.expire(redis_key, self.window_seconds + 1)
        
        return True

    def get_remaining(self, key: str) -> int:
        """
        Get remaining requests for the given key.
        
        Args:
            key: Identifier (IP address or user ID)
            
        Returns:
            Number of remaining requests in current window
        """
        redis_key = self._get_redis_key(key)
        now = time.time()
        cutoff_time = now - self.window_seconds
        
        # Count requests in current window
        count = self.redis.zcount(redis_key, cutoff_time, now)
        
        return max(0, self.max_requests - count)

    def reset(self, key: Optional[str] = None) -> None:
        """
        Reset rate limit for a key. If key is None, reset all keys.
        
        Args:
            key: Identifier to reset, or None to reset all
        """
        if key is None:
            # Delete all rate limit keys
            pattern = f"{self.key_prefix}*"
            cursor = 0
            while True:
                cursor, keys = self.redis.scan(cursor, match=pattern, count=100)
                if keys:
                    self.redis.delete(*keys)
                if cursor == 0:
                    break
        else:
            redis_key = self._get_redis_key(key)
            self.redis.delete(redis_key)
