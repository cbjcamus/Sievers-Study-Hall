import os
from typing import Optional


class RateLimitConfig:
    """Configuration for rate limiting on LLM-based exercises."""

    ENABLED = os.environ.get("RATE_LIMIT_ENABLED", "true").lower() in ("true", "1", "yes")
    BACKEND = os.environ.get("RATE_LIMIT_BACKEND", "memory").lower()
    # only used if BACKEND="redis"
    REDIS_URL = os.environ.get("RATE_LIMIT_REDIS_URL", "redis://localhost:6379/0")
    UNAUTHENTICATED_MAX_REQUESTS = int(
        os.environ.get("RATE_LIMIT_UNAUTHENTICATED_MAX_REQUESTS", "50")
    )
    AUTHENTICATED_MAX_REQUESTS = int(
        os.environ.get("RATE_LIMIT_AUTHENTICATED_MAX_REQUESTS", "100")
    )
    WINDOW_SECONDS = int(os.environ.get("RATE_LIMIT_WINDOW_SECONDS", "3600"))

    @classmethod
    def to_dict(cls) -> dict:
        """Return configuration as dictionary."""
        return {
            "enabled": cls.ENABLED,
            "backend": cls.BACKEND,
            "redis_url": cls.REDIS_URL if cls.BACKEND == "redis" else None,
            "unauthenticated_max_requests": cls.UNAUTHENTICATED_MAX_REQUESTS,
            "authenticated_max_requests": cls.AUTHENTICATED_MAX_REQUESTS,
            "window_seconds": cls.WINDOW_SECONDS,
        }

    @classmethod
    def get_backend_class(cls):
        """
        Get the rate limiter backend class based on configuration.
        
        Returns:
            Rate limiter class (InMemoryRateLimiter or RedisRateLimiter)
            
        Raises:
            ValueError: If backend is not recognized or Redis connection fails
        """
        if cls.BACKEND == "memory":
            from users.rate_limiting.limiter import InMemoryRateLimiter
            return InMemoryRateLimiter
        elif cls.BACKEND == "redis":
            try:
                import redis
            except ImportError:
                raise ValueError(
                    "Redis backend selected but 'redis' package not installed. "
                    "Install with: pip install redis"
                )
            
            from users.rate_limiting.redis_limiter import RedisRateLimiter
            
            try:
                redis_client = redis.from_url(cls.REDIS_URL)
                redis_client.ping()  # Test connection
            except Exception as e:
                raise ValueError(
                    f"Failed to connect to Redis at {cls.REDIS_URL}: {e}"
                )
            
            # Return a wrapper class that includes the redis client
            class ConfiguredRedisRateLimiter(RedisRateLimiter):
                def __init__(self, max_requests: int, window_seconds: int):
                    super().__init__(max_requests, window_seconds, redis_client)
            
            return ConfiguredRedisRateLimiter
        else:
            raise ValueError(
                f"Unknown rate limit backend: {cls.BACKEND}. "
                "Must be 'memory' or 'redis'."
            )
