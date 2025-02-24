FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN pip install poetry && poetry install --no-dev

COPY . .

CMD ["uvicorn", "graphkb.api.main:app", "--host", "0.0.0.0", "--port", "8000"]