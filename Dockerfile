# syntax=docker/dockerfile:1

# Install Python Image
FROM python:3.9.17

WORKDIR /app

# Install dependencies
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only main --no-root --no-directory && \
    rm -rf ~/.cache/pypoetry/

# Copy src file
COPY . .

CMD uvicorn src.app:app --host 0.0.0.0 --port 8000