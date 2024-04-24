FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

ARG PIP_ROOT_USER_ACTION='ignore'
ARG PIP_ROOT_USER_ACTION=${PIP_ROOT_USER_ACTION}
ENV PIP_ROOT_USER_ACTION ${PIP_ROOT_USER_ACTION}

ARG POETRY_VIRTUALENVS_CREATE='false'
ARG POETRY_VIRTUALENVS_CREATE=${POETRY_VIRTUALENVS_CREATE}
ENV POETRY_VIRTUALENVS_CREATE ${POETRY_VIRTUALENVS_CREATE}

WORKDIR /app
COPY poetry.lock .
COPY pyproject.toml .
RUN pip install -U pip
RUN pip install poetry==1.7.0
RUN poetry lock
RUN poetry install --no-root --without dev
COPY . .

ARG WORKERS='4'
ARG WORKERS=${WORKERS}
ENV WORKERS ${WORKERS}

CMD alembic upgrade head && gunicorn --workers $WORKERS --forwarded-allow-ips='*' --worker-class uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000