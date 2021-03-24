#FROM balenalib/%%BALENA_MACHINE_NAME%%-alpine-golang:1.14
FROM balenalib/raspberrypi4-64-alpine-golang:1.14-run as jsonnet

RUN install_packages git && \
    go get -v github.com/jsonnet-bundler/jsonnet-bundler/cmd/jb && \
    go get -v github.com/google/go-jsonnet/cmd/jsonnet


WORKDIR /app
COPY ./jsonnetfile.json* ./
RUN jb install