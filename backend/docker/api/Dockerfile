#
FROM python:3.9-slim AS builder
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1
RUN pip install poetry
RUN python3 -m venv /venv
COPY ./pyproject.toml .
COPY ./poetry.lock .
RUN  . ./venv/bin/activate && poetry install --no-dev --no-root

#
FROM builder as deploy
ENV VIRTUAL_ENV=/app/venv \
    PATH="/app/venv/bin:$PATH" \
    PYTHONPATH="/app/src"
WORKDIR /app
COPY --from=builder /venv /app/venv
COPY src /app
COPY start.sh /app
RUN chmod +x /app/start.sh
CMD ["./start.sh"]
