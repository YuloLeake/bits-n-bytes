FROM local:base

COPY requirements.txt requirements.txt
RUN printenv
RUN pip install -r requirements.txt

RUN pip install pipdeptree==2.23.1

# Run pipdeptree in the context of the venv set by the base image
# https://github.com/tox-dev/pipdeptree/blob/2.23.1/README.md#running-in-virtualenvs
CMD [ "pipdeptree", "--python", "auto" ]