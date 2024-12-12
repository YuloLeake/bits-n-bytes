FROM debian:bookworm-slim AS build

ENV APP_PATH=/opt/app

# Set venv based on https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
# you could also just do something like
# VIRTUAL_ENV=${APP_PATH}/.venv uv pip install -r requirements.txt
# in below instead of setting it ahead
ENV VIRTUAL_ENV=${APP_PATH}/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --from=ghcr.io/astral-sh/uv:0.5.7 /uv /uvx /bin/

RUN uvx --python 3.12 pycowsay 'hello world!'

RUN uv venv --python 3.12 $VIRTUAL_ENV

WORKDIR ${APP_PATH}
COPY requirements.txt .
RUN uv pip install -r requirements.txt

FROM gcr.io/distroless/base-debian12

# Copy primitive commands as needed
# COPY --from=busybox:1.37.0-uclibc /bin/sh /bin/sh
# COPY --from=busybox /bin/mkdir /bin/mkdir
# COPY --from=busybox /bin/mkdir /bin/ls
# COPY --from=busybox /bin/cat /bin/cat

ENV APP_PATH=/opt/app
ENV VIRTUAL_ENV=${APP_PATH}/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR ${APP_PATH}

COPY --from=build ${APP_PATH} ${APP_PATH}
# Required to include the actual python binary
# or by copying /root/.local/share/uv/python for specifically python stuff
COPY --from=build /root/.local/share/uv /root/.local/share/uv

CMD ["python", "-V"]