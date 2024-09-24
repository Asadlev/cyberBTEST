FROM python:3.11

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy asyncpg requests python-telegram-bot

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
