# Sievers Study Hall

Any question? https://substack.com/home/post/p-165326616

Any other question? sieversstudyhall@gmail.com

## Running with Docker

### Development

```bash
docker-compose -f docker-compose.dev.yml up --build
```

App available at `http://localhost:5000` with auto-reload on code changes.

### Production

Create a `.env` file:
```bash
FLASK_SECRET_KEY=your-secure-key-here
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

Then run:
```bash
docker-compose up --build
```

## Running tests

```bash
# With Docker
docker-compose -f docker-compose.dev.yml exec app python -m pytest tests/

# Without Docker
python -m venv .venv
.venv/bin/pip install -r requirements.txt pytest
.venv/bin/python -m pytest tests/
```
