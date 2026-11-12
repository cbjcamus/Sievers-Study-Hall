"""In-memory rate limiter backend."""

import time
from collections import defaultdict
from typing import Optional
from threading import Lock

from users.rate_limiting.backend import RateLimiterBackend


class InMemoryRateLimiter(RateLimiterBackend):
    """
    In-memory rate limiter for single-instance deployments.
    Tracks requests per key (IP or user ID) and enforces rate limits.
    """

    def __init__(self, max_requests: int, window_seconds: int):
        """
        Initialize rate limiter.
        
        Args:
            max_requests: Maximum number of requests allowed in the time window
            window_seconds: Time window in seconds
        """
        super().__init__(max_requests, window_seconds)
        self.requests = defaultdict(list)  # key -> list of timestamps
        self.lock = Lock()

    def is_allowed(self, key: str) -> bool:
        """
        Check if a request from the given key is allowed.
        
        Args:
            key: Identifier (IP address or user ID)
            
        Returns:
            True if request is allowed, False if rate limit exceeded
        """
        with self.lock:
            now = time.time()
            cutoff_time = now - self.window_seconds
            
            # Remove old timestamps outside the window
            self.requests[key] = [
                timestamp for timestamp in self.requests[key]
                if timestamp > cutoff_time
            ]
            
            # Check if limit exceeded
            if len(self.requests[key]) >= self.max_requests:
                return False
            
            # Record this request
            self.requests[key].append(now)
            return True

    def get_remaining(self, key: str) -> int:
        """
        Get remaining requests for the given key.
        
        Args:
            key: Identifier (IP address or user ID)
            
        Returns:
            Number of remaining requests in current window
        """
        with self.lock:
            now = time.time()
            cutoff_time = now - self.window_seconds
            
            # Count requests in current window
            current_requests = len([
                timestamp for timestamp in self.requests[key]
                if timestamp > cutoff_time
            ])
            
            return max(0, self.max_requests - current_requests)

    def reset(self, key: Optional[str] = None) -> None:
        """
        Reset rate limit for a key. If key is None, reset all keys.
        
        Args:
            key: Identifier to reset, or None to reset all
        """
        with self.lock:
            if key is None:
                self.requests.clear()
            else:
                self.requests[key] = []


# Backwards compatibility alias
RateLimiter = InMemoryRateLimiter
