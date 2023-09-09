FROM python:3.10.5

ENV POETRY_VERSION=1.6.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

ARG UID=1000
ARG GID=1000

RUN groupadd -g "${GID}" python \
  && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python
WORKDIR /home/python

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
	&& $POETRY_VENV/bin/pip install -U pip setuptools \
	&& $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

USER python:python
ENV PATH="/home/${USER}/.local/bin:${PATH}"
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Set PYENV_HOME to a directory where the user has write permissions
ENV PYENV_HOME=/home/python/.cache/virtualenvs

WORKDIR /app

# Copy Dependencies
COPY --chown=python:python poetry.lock pyproject.toml ./

# Install Dependencies
RUN poetry env use 3.10.5 && poetry install --no-interaction --no-cache --without dev

# Copy Application
COPY --chown=python:python . /app

# Run Application
EXPOSE 5000
CMD [ "poetry", "run", "python", "src/app.py" ]