# Sievers Study Hall

Any question? https://substack.com/home/post/p-165326616

Any other question? sieversstudyhall@gmail.com

## Rate Limiting

Exercise submission endpoints are protected with rate limiting to prevent abuse of the LLM API. By default, an in-memory backend stores limits per IP address or user ID.

### Configuration

Set these environment variables to customize rate limiting:

```bash
RATE_LIMIT_ENABLED=true                          # Enable/disable (default: true)
RATE_LIMIT_BACKEND=memory                        # `memory` or `redis` (default: memory)
RATE_LIMIT_UNAUTHENTICATED_MAX=20                # Requests/hour for unauthenticated (default: 50)
RATE_LIMIT_AUTHENTICATED_MAX=100                 # Requests/hour for authenticated (default: 100)
RATE_LIMIT_WINDOW_SECONDS=3600                   # Time window in seconds (default: 3600)
```

### Using Redis Backend

Instead of storing in memory, Redis can be used to store rate limits to allow multiple instances of the app to be deployed with the:

```bash
RATE_LIMIT_BACKEND=redis
RATE_LIMIT_REDIS_URL=redis://<redis domain>:6379/0
```

## Running tests

```bash
python -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/python -m pytest tests/
```
