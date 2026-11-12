FROM python:3.12-slim AS base

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM base AS development

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

COPY . .

RUN mkdir -p instance

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

FROM base AS production

RUN useradd -m -u 1000 appuser

COPY --chown=appuser:appuser app.py .
COPY --chown=appuser:appuser users/ users/
COPY --chown=appuser:appuser webapp/ webapp/
COPY --chown=appuser:appuser data/ data/

RUN mkdir -p instance && chown -R appuser:appuser instance

USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000', timeout=2)"

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "60", "--access-logfile", "-", "--error-logfile", "-", "app:app"]