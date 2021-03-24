### TODO: redesign for multi stage build (as example)
### https://github.com/zinen/docker-alpine-pigpiod/blob/main/Dockerfile

FROM balenalib/raspberrypi4-64-ubuntu:bionic-build

RUN install_packages unzip #build-base

WORKDIR /app

ARG PIGPIOD_VERSION=78
RUN wget https://github.com/joan2937/pigpio/archive/v${PIGPIOD_VERSION}.zip 
RUN unzip v${PIGPIOD_VERSION}.zip

WORKDIR /app/pigpio-${PIGPIOD_VERSION}

# Fix for compiling on Alpine, https://github.com/joan2937/pigpio/issues/107
# RUN sed -i -e 's/ldconfig/echo ldconfig disabled/g' Makefile
RUN make
RUN make install

ENV UDEV 1

CMD ["pigpiod", "-g"]