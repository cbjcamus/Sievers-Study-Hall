"""
Tests for Redis rate limiter backend (users/rate_limiting/redis_limiter.py).

Covers:
- Redis connection and initialization
- Requests within limit are allowed
- Requests exceeding limit are blocked
- Different keys maintain separate limits
- Time window expiration
- Remaining request counting
- Resetting limits
"""

import pytest
import time


def test_redis_limiter_allows_requests_within_limit(redis_client):
    """Test that Redis limiter allows requests within limit."""
    from users.rate_limiting.redis_limiter import RedisRateLimiter
    
    limiter = RedisRateLimiter(max_requests=3, window_seconds=60, redis_client=redis_client)
    
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is True


def test_redis_limiter_blocks_requests_exceeding_limit(redis_client):
    """Test that Redis limiter blocks requests exceeding limit."""
    from users.rate_limiting.redis_limiter import RedisRateLimiter
    
    limiter = RedisRateLimiter(max_requests=2, window_seconds=60, redis_client=redis_client)
    
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is False
    assert limiter.is_allowed("user1") is False


def test_redis_limiter_separate_keys(redis_client):
    """Test that different keys have separate limits."""
    from users.rate_limiting.redis_limiter import RedisRateLimiter
    
    limiter = RedisRateLimiter(max_requests=2, window_seconds=60, redis_client=redis_client)
    
    # User1 uses up their limit
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is False
    
    # User2 should still have limit available
    assert limiter.is_allowed("user2") is True
    assert limiter.is_allowed("user2") is True
    assert limiter.is_allowed("user2") is False


def test_redis_limiter_get_remaining(redis_client):
    """Test getting remaining request count."""
    from users.rate_limiting.redis_limiter import RedisRateLimiter
    
    limiter = RedisRateLimiter(max_requests=5, window_seconds=60, redis_client=redis_client)
    
    assert limiter.get_remaining("user1") == 5
    limiter.is_allowed("user1")
    assert limiter.get_remaining("user1") == 4
    limiter.is_allowed("user1")
    assert limiter.get_remaining("user1") == 3


def test_redis_limiter_reset_single_key(redis_client):
    """Test resetting rate limit for a single key."""
    from users.rate_limiting.redis_limiter import RedisRateLimiter
    
    limiter = RedisRateLimiter(max_requests=2, window_seconds=60, redis_client=redis_client)
    
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is False
    
    limiter.reset("user1")
    
    assert limiter.is_allowed("user1") is True
    assert limiter.get_remaining("user1") == 1


def test_redis_limiter_reset_all_keys(redis_client):
    """Test resetting rate limit for all keys."""
    from users.rate_limiting.redis_limiter import RedisRateLimiter
    
    limiter = RedisRateLimiter(max_requests=1, window_seconds=60, redis_client=redis_client)
    
    limiter.is_allowed("user1")
    limiter.is_allowed("user2")
    
    assert limiter.is_allowed("user1") is False
    assert limiter.is_allowed("user2") is False
    
    limiter.reset()
    
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user2") is True


def test_redis_limiter_window_expiration(redis_client):
    """Test that old requests are forgotten after window expires."""
    from users.rate_limiting.redis_limiter import RedisRateLimiter
    
    limiter = RedisRateLimiter(max_requests=2, window_seconds=1, redis_client=redis_client)
    
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is False
    
    # Wait for window to expire
    time.sleep(1.1)
    
    # Should be allowed again
    assert limiter.is_allowed("user1") is True
