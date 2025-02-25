FROM python:3.9-slim

WORKDIR /app

# Definizione dei volumi
VOLUME ["/app/src", "/app/tests", "/app/reports"]

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest pytest-cov

# Crea directory per i report
RUN mkdir -p /app/reports
RUN chmod -R 777 /app/reports

CMD ["pytest", "--cov=src", "--cov-report=html:/app/reports/htmlcov", "tests/"]