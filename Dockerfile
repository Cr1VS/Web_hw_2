FROM python:3.11


RUN curl -sSL https://install.python-poetry.org/ | python -
RUN pip install poetry


ENV PATH="${PATH}:/root/.local/bin"


WORKDIR /app


COPY pyproject.toml poetry.lock /app/


RUN poetry config virtualenvs.create true && \
    poetry install --no-dev


COPY . /app


EXPOSE 3100


CMD ["sleep", "infinity"]