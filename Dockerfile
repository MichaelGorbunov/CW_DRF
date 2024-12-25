FROM python:3.12-slim

# Настраиваем переменные окружения для poetry
ENV POETRY_VERSION=1.8.5
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# Устанавливаем poetry
RUN python3 -m venv $POETRY_VENV \
	&& $POETRY_VENV/bin/pip install -U pip setuptools \
	&& $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Добавляем poetry в переменную окружения PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app

# Установка зависимостей
COPY poetry.lock pyproject.toml ./
RUN poetry install

# Копирование и запуск приложения (в данном случае просто кода)
COPY . /app
#CMD [ "poetry", "run", "python3", "manage.py", "runserver" ]
#CMD ["sh"]