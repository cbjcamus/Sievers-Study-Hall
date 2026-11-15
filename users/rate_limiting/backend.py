"""Abstract base class for rate limiters."""

from abc import ABC, abstractmethod
from typing import Optional


class RateLimiterBackend(ABC):
    """Abstract base class for rate limiting backends."""

    def __init__(self, max_requests: int, window_seconds: int):
        """
        Initialize rate limiter.
        
        Args:
            max_requests: Maximum number of requests allowed in the time window
            window_seconds: Time window in seconds
        """
        self.max_requests = max_requests
        self.window_seconds = window_seconds

    @abstractmethod
    def is_allowed(self, key: str) -> bool:
        """
        Check if a request from the given key is allowed.
        
        Args:
            key: Identifier (IP address or user ID)
            
        Returns:
            True if request is allowed, False if rate limit exceeded
        """
        pass

    @abstractmethod
    def get_remaining(self, key: str) -> int:
        """
        Get remaining requests for the given key.
        
        Args:
            key: Identifier (IP address or user ID)
            
        Returns:
            Number of remaining requests in current window
        """
        pass

    @abstractmethod
    def reset(self, key: Optional[str] = None) -> None:
        """
        Reset rate limit for a key. If key is None, reset all keys.
        
        Args:
            key: Identifier to reset, or None to reset all
        """
        pass
