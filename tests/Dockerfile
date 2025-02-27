FROM python:3.9-slim

WORKDIR /app

# Copia i file necessari
COPY requirements.txt .
COPY .coveragerc .

# Copia il codice sorgente e i test
COPY SimulatePosition/ ./SimulatePosition


# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest pytest-cov

# Crea directory per i report
RUN mkdir -p /app/reports
RUN chmod -R 777 /app/reports

# Definizione dei volumi per persistere i report
VOLUME ["/app/reports"]

# Esegue i test con coverage
CMD ["pytest", "--cov=SimulatePosition", "--cov-report=html:/app/reports/htmlcov", "tests/", "--cov-config=.coveragerc"]


# # Costruisci l'immagine
# docker build -t python-test-coverage -f tests/Dockerfile .

# # Esegui i test e monta un volume per accedere ai report
# docker run --rm -v $(pwd)/reports:/app/reports python-test-coverage