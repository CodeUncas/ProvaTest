[![Python Tests & Quality Checks](https://github.com/CodeUncas/ProvaTest/actions/workflows/main.yml/badge.svg)](https://github.com/CodeUncas/ProvaTest/actions/workflows/main.yml)

[![Coverage Status](https://coveralls.io/repos/github/CodeUncas/ProvaTest/badge.svg?branch=main)](https://coveralls.io/github/CodeUncas/ProvaTest?branch=main)

# README.md content

# Python Test Project

Questo progetto è un esempio di configurazione per eseguire test in Python utilizzando sia `unittest` che `pytest`.

## Struttura del Progetto

```
python-test-project
├── src
│   └── __init__.py
├── tests
│   ├── __init__.py
│   ├── test_unittest.py
│   └── test_pytest.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Requisiti

Assicurati di avere Python 3.x installato. Puoi installare le dipendenze necessarie eseguendo:

```
pip install -r requirements.txt
```

## Esecuzione dei Test

Per eseguire i test, puoi utilizzare i seguenti comandi:

### Unittest

Per eseguire i test con `unittest`, utilizza il comando:

```
python -m unittest discover -s tests
```

### Pytest

Per eseguire i test con `pytest`, utilizza il comando:

```
pytest
```

## Docker

Per costruire e eseguire il progetto in un contenitore Docker, utilizza i seguenti comandi:

### Costruzione dell'immagine

```
docker build -t python-test-project .
```

### Esecuzione dei test nel contenitore

```
docker run --rm python-test-project
```

## Contribuire

Se desideri contribuire a questo progetto, sentiti libero di aprire una pull request o segnalare problemi.
