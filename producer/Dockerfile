FROM python:3.9

RUN python -m pip install poetry

COPY producer/  producer/
COPY pyproject.toml pyproject.toml

RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "-m", "producer"]
