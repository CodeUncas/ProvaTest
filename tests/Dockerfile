FROM python:3.9-slim

WORKDIR /app

# Copia i file necessari
COPY tests/requirements.txt .
COPY tests/.coveragerc .
COPY tests/pylintrc .
RUN mkdir -p app/SimulatePositions
RUN mkdir -p app/FlinkController
RUN mkdir -p app/tests
COPY ./tests /app/tests
# Copia il codice sorgente e i test
COPY ./SimulatePositions /app/SimulatePositions
COPY ./FlinkController /app/FlinkController

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest pytest-cov coveralls pylint

# Crea directory per i report

# Esegue i test con coverage
CMD ["sh","-c","pylint --rcfile=tests/pylintrc . > pylint_report.txt; pytest --cov=SimulatePositions --cov=FlinkController --cov-report=xml:coverage.xml tests/ --cov-config=.coveragerc "]


# # Costruisci l'immagine
# docker build -t python-test-coverage -f tests/Dockerfile .

# # Esegui i test e monta un volume per accedere ai report
# docker run --rm -v $(pwd)/reports:/app/reports python-test-coverage