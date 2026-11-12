"""
Unit tests for the in-memory rate limiter (users/rate_limiting/limiter.py).

Covers:
- Requests within limit are allowed
- Requests exceeding limit are blocked
- Different keys maintain separate limits
- Time window expiration
- Getting remaining request counts
- Resetting limits
"""

import time
import threading
import pytest
from users.rate_limiting.limiter import RateLimiter


def test_allows_requests_within_limit():
    """Test that requests within limit are allowed."""
    limiter = RateLimiter(max_requests=3, window_seconds=60)
    
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is True


def test_blocks_requests_exceeding_limit():
    """Test that requests exceeding limit are blocked."""
    limiter = RateLimiter(max_requests=2, window_seconds=60)
    
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is False
    assert limiter.is_allowed("user1") is False


def test_separate_keys_have_separate_limits():
    """Test that different keys have separate limits."""
    limiter = RateLimiter(max_requests=2, window_seconds=60)
    
    # User1 uses up their limit
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is False
    
    # User2 should still have limit available
    assert limiter.is_allowed("user2") is True
    assert limiter.is_allowed("user2") is True
    assert limiter.is_allowed("user2") is False


def test_window_resets_after_expiration():
    """Test that old requests are forgotten after window expires."""
    limiter = RateLimiter(max_requests=2, window_seconds=1)
    
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is False
    
    # Wait for window to expire
    time.sleep(1.1)
    
    # Should be allowed again
    assert limiter.is_allowed("user1") is True


def test_get_remaining_request_count():
    """Test getting remaining request count."""
    limiter = RateLimiter(max_requests=5, window_seconds=60)
    
    assert limiter.get_remaining("user1") == 5
    limiter.is_allowed("user1")
    assert limiter.get_remaining("user1") == 4
    limiter.is_allowed("user1")
    assert limiter.get_remaining("user1") == 3


def test_reset_single_key():
    """Test resetting rate limit for a single key."""
    limiter = RateLimiter(max_requests=2, window_seconds=60)
    
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is False
    
    limiter.reset("user1")
    
    assert limiter.is_allowed("user1") is True
    assert limiter.get_remaining("user1") == 1


def test_reset_all_keys():
    """Test resetting rate limit for all keys."""
    limiter = RateLimiter(max_requests=1, window_seconds=60)
    
    limiter.is_allowed("user1")
    limiter.is_allowed("user2")
    
    assert limiter.is_allowed("user1") is False
    assert limiter.is_allowed("user2") is False
    
    limiter.reset()
    
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user2") is True


def test_multiple_keys_independent():
    """Test that multiple keys maintain independent limits."""
    limiter = RateLimiter(max_requests=2, window_seconds=60)
    
    # Fill up user1's limit
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is True
    
    # User2 should be independent
    assert limiter.is_allowed("user2") is True
    assert limiter.is_allowed("user2") is True
    
    # Both should now be blocked
    assert limiter.is_allowed("user1") is False
    assert limiter.is_allowed("user2") is False


def test_thread_safety():
    """Test that rate limiter is thread-safe."""
    limiter = RateLimiter(max_requests=100, window_seconds=60)
    results = []
    lock = threading.Lock()
    
    def make_requests(key, count):
        for _ in range(count):
            result = limiter.is_allowed(key)
            with lock:
                results.append(result)
    
    threads = [
        threading.Thread(target=make_requests, args=("user1", 50)),
        threading.Thread(target=make_requests, args=("user1", 50)),
    ]
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
    
    # Should have exactly 100 True and 0 False
    assert results.count(True) == 100
    assert results.count(False) == 0


def test_window_boundary_conditions():
    """Test behavior at window boundaries."""
    limiter = RateLimiter(max_requests=2, window_seconds=1)
    
    # Make two requests
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is True
    assert limiter.is_allowed("user1") is False
    
    # Wait just under window
    time.sleep(0.5)
    assert limiter.is_allowed("user1") is False
    
    # Wait past window
    time.sleep(0.6)
    assert limiter.is_allowed("user1") is True
