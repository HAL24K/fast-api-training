FROM python:3.9-slim

RUN apt-get update && pip install --upgrade pip && pip install fastapi uvicorn redis

EXPOSE 80

COPY app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]