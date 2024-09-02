FROM python:3.12.5-slim-bookworm

RUN pip install poetry

COPY src /usr/src
WORKDIR /usr/src

# Create and activate a venv by setting the VIRTUAL_ENV and the PATH env vars.
# https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
ENV VIRTUAL_ENV=/usr/src/my_venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Poetry will use the venv when installing while venv is active.
# https://github.com/python-poetry/poetry/issues/263#issuecomment-1404129650
RUN poetry install

CMD ["poetry", "run", "python", "main.py"]