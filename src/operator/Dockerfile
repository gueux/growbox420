#FROM balenalib/%%BALENA_MACHINE_NAME%%-alpine-python:3.9.0
FROM balenalib/raspberrypi4-64-alpine-python:3.9.0

RUN install_packages build-base

# Defines our working directory in container
WORKDIR /app

COPY ./requirements.txt ./
RUN pip3 install --no-cache-dir -r ./requirements.txt

COPY . ./

CMD [ "python3", "start.py" ]