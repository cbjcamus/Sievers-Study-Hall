from functools import wraps
from flask import request, jsonify
from flask_login import current_user

from users.rate_limiting.config import RateLimitConfig


# Global rate limiters (initialized lazily)
_unauthenticated_limiter = None
_authenticated_limiter = None


def _get_limiters():
    """Get or create the rate limiters."""
    global _unauthenticated_limiter, _authenticated_limiter
    
    if _unauthenticated_limiter is None:
        backend_class = RateLimitConfig.get_backend_class()
        _unauthenticated_limiter = backend_class(
            max_requests=RateLimitConfig.UNAUTHENTICATED_MAX_REQUESTS,
            window_seconds=RateLimitConfig.WINDOW_SECONDS,
        )
        _authenticated_limiter = backend_class(
            max_requests=RateLimitConfig.AUTHENTICATED_MAX_REQUESTS,
            window_seconds=RateLimitConfig.WINDOW_SECONDS,
        )
    
    return _unauthenticated_limiter, _authenticated_limiter


def get_client_key() -> str:
    """
    Get the key for rate limiting: user ID if authenticated, otherwise IP address.
    
    Returns:
        User ID or IP address
    """
    if current_user and current_user.is_authenticated:
        return f"user:{current_user.id}"
    return f"ip:{request.remote_addr}"


def rate_limit_exercise_submission(f):
    """
    Decorator to rate limit exercise submission endpoints.
    
    Returns:
        429 Too Many Requests if rate limit exceeded
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not RateLimitConfig.ENABLED:
            return f(*args, **kwargs)

        key = get_client_key()
        
        # Choose limiter based on authentication
        unauth_limiter, auth_limiter = _get_limiters()
        
        if current_user and current_user.is_authenticated:
            limiter = auth_limiter
        else:
            limiter = unauth_limiter

        if not limiter.is_allowed(key):
            remaining = limiter.get_remaining(key)
            return jsonify({
                "error": "Rate limit exceeded",
                "message": f"Too many requests. Try again in {RateLimitConfig.WINDOW_SECONDS} seconds.",
                "remaining_requests": remaining,
            }), 429

        return f(*args, **kwargs)

    return decorated_function


def reset_rate_limit(key: str = None) -> None:
    """
    Reset rate limit for a key or all keys.
    
    Args:
        key: Optional key to reset. If None, resets all keys.
    """
    unauth_limiter, auth_limiter = _get_limiters()
    unauth_limiter.reset(key)
    auth_limiter.reset(key)


def get_rate_limit_status(key: str = None) -> dict:
    """
    Get rate limit status for a key.
    
    Args:
        key: Optional key. If None, uses current client key.
        
    Returns:
        Dictionary with status info
    """
    if key is None:
        key = get_client_key()

    unauth_limiter, auth_limiter = _get_limiters()
    
    if current_user and current_user.is_authenticated:
        limiter = auth_limiter
        max_requests = RateLimitConfig.AUTHENTICATED_MAX_REQUESTS
    else:
        limiter = unauth_limiter
        max_requests = RateLimitConfig.UNAUTHENTICATED_MAX_REQUESTS

    remaining = limiter.get_remaining(key)
    
    return {
        "key": key,
        "remaining_requests": remaining,
        "max_requests": max_requests,
        "window_seconds": RateLimitConfig.WINDOW_SECONDS,
    }
