FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Установка Playwright 
RUN python -m playwright install-deps && \
    python -m playwright install chromium

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]