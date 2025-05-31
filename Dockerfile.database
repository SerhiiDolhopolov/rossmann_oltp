FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY database ./database
COPY rossmann_oltp_models ./rossmann_oltp_models

ENV PYTHONPATH=/app

CMD ["python", "-u", "database/main.py"]