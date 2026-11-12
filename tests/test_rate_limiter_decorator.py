"""
Tests for rate limiting decorator (users/rate_limiting/decorator.py).

Covers:
- Decorator allows/blocks requests based on limits
- Disabled config bypasses rate limiting
- Authenticated users get higher limits than unauthenticated
- Different IP addresses maintain separate limits
- Rate limit response format
"""

import json
import pytest
from flask_login import login_user
from unittest.mock import patch

from users.rate_limiting.decorator import (
    rate_limit_exercise_submission,
    reset_rate_limit,
    get_rate_limit_status,
    get_client_key,
)
from users.rate_limiting.config import RateLimitConfig
from conftest import make_test_user


def test_decorator_allows_requests_within_limit(app):
    """Test that decorator allows requests within limit."""
    reset_rate_limit()
    
    client = app.test_client()
    
    # Should allow up to UNAUTHENTICATED_MAX_REQUESTS
    for _ in range(RateLimitConfig.UNAUTHENTICATED_MAX_REQUESTS):
        response = client.post('/test-endpoint', environ_base={'REMOTE_ADDR': '127.0.0.1'})
        assert response.status_code == 200
        assert response.json == {"status": "ok"}
    
    # Next request should be blocked
    response = client.post('/test-endpoint', environ_base={'REMOTE_ADDR': '127.0.0.1'})
    assert response.status_code == 429
    assert "Rate limit exceeded" in response.json["error"]


def test_decorator_disabled_by_config(app):
    """Test that decorator respects ENABLED config."""
    reset_rate_limit()
    
    client = app.test_client()
    
    with patch('users.rate_limiting.decorator.RateLimitConfig.ENABLED', False):
        # Should allow all requests when disabled
        for _ in range(100):
            response = client.post('/test-endpoint', environ_base={'REMOTE_ADDR': '127.0.0.1'})
            assert response.status_code == 200


def test_authenticated_users_get_higher_limits(app):
    """Test that authenticated users get higher limits."""
    reset_rate_limit()
    
    user = make_test_user("auth@example.com")
    client = app.test_client()
    
    with app.test_request_context():
        login_user(user)
        
        # Should allow up to AUTHENTICATED_MAX_REQUESTS (higher than unauthenticated)
        for _ in range(RateLimitConfig.AUTHENTICATED_MAX_REQUESTS):
            response = client.post('/test-endpoint', environ_base={'REMOTE_ADDR': '127.0.0.1'})
            assert response.status_code == 200
        
        # Next request should be blocked
        response = client.post('/test-endpoint', environ_base={'REMOTE_ADDR': '127.0.0.1'})
        assert response.status_code == 429


def test_different_ips_have_separate_limits(app):
    """Test that different IPs have separate rate limits."""
    reset_rate_limit()
    
    client = app.test_client()
    
    # IP 1 uses up their limit
    for _ in range(RateLimitConfig.UNAUTHENTICATED_MAX_REQUESTS):
        response = client.post('/test-endpoint', environ_base={'REMOTE_ADDR': '192.168.1.1'})
        assert response.status_code == 200
    
    # IP 1 should be blocked
    response = client.post('/test-endpoint', environ_base={'REMOTE_ADDR': '192.168.1.1'})
    assert response.status_code == 429
    
    # IP 2 should still have requests available
    response = client.post('/test-endpoint', environ_base={'REMOTE_ADDR': '192.168.1.2'})
    assert response.status_code == 200


def test_get_client_key_authenticated(app):
    """Test get_client_key with authenticated user."""
    user = make_test_user("key@example.com")
    
    with app.test_request_context(environ_base={'REMOTE_ADDR': '127.0.0.1'}):
        login_user(user)
        key = get_client_key()
        assert key == f"user:{user.id}"


def test_get_client_key_unauthenticated(app):
    """Test get_client_key with unauthenticated user."""
    with app.test_request_context(environ_base={'REMOTE_ADDR': '10.0.0.1'}):
        key = get_client_key()
        assert key == "ip:10.0.0.1"


def test_rate_limit_response_format(app):
    """Test that rate limit response has correct format."""
    reset_rate_limit()
    
    client = app.test_client()
    
    # Exhaust limit
    for _ in range(RateLimitConfig.UNAUTHENTICATED_MAX_REQUESTS):
        client.post('/test-endpoint', environ_base={'REMOTE_ADDR': '127.0.0.1'})
    
    # Get blocked response
    response = client.post('/test-endpoint', environ_base={'REMOTE_ADDR': '127.0.0.1'})
    
    assert response.status_code == 429
    data = response.json
    assert "error" in data
    assert "message" in data
    assert "remaining_requests" in data


def test_reset_rate_limit(app):
    """Test resetting rate limit."""
    reset_rate_limit()
    
    client = app.test_client()
    
    # Exhaust limit
    for _ in range(RateLimitConfig.UNAUTHENTICATED_MAX_REQUESTS):
        client.post('/test-endpoint', environ_base={'REMOTE_ADDR': '127.0.0.1'})
    
    # Should be blocked
    response = client.post('/test-endpoint', environ_base={'REMOTE_ADDR': '127.0.0.1'})
    assert response.status_code == 429
    
    # Reset
    reset_rate_limit("ip:127.0.0.1")
    
    # Should work again
    response = client.post('/test-endpoint', environ_base={'REMOTE_ADDR': '127.0.0.1'})
    assert response.status_code == 200


def test_get_rate_limit_status(app):
    """Test getting rate limit status."""
    reset_rate_limit()
    
    with app.test_request_context(environ_base={'REMOTE_ADDR': '127.0.0.1'}):
        status = get_rate_limit_status("ip:127.0.0.1")
        
        assert status["key"] == "ip:127.0.0.1"
        assert status["remaining_requests"] == RateLimitConfig.UNAUTHENTICATED_MAX_REQUESTS
        assert status["max_requests"] == RateLimitConfig.UNAUTHENTICATED_MAX_REQUESTS
        assert status["window_seconds"] == RateLimitConfig.WINDOW_SECONDS

