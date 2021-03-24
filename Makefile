APPLICATION=Microgreen420

BALENA_OS_ARCH=raspberrypi4-64
BALENA_OS_VERSION=v12.3.0
BALENA_OS_IMAGE_DEV=2.60.1+rev1.dev 
BALENA_OS_IMAGE_PROD=2.67.3+rev4

dev:
	balena os download raspberrypi4-64 -o ~/Downloads/balena-cloud-$${BALENA_OS_ARCH}-$${BALENA_OS_IMAGE_DEV}-${BALENA_OS_VERSION}.img --version $${BALENA_OS_IMAGE_DEV}
	balena os configure ~/Downloads/balena-cloud-$${BALENA_OS_ARCH}-$${BALENA_OS_IMAGE_DEV}-${BALENA_OS_VERSION}.img --app $${APPLICATION}

prod:
	balena os download raspberrypi4-64 -o ~/Downloads/balena-cloud-$${BALENA_OS_ARCH}-$${BALENA_OS_IMAGE_PROD}-${BALENA_OS_VERSION}.img --version $${BALENA_OS_IMAGE_PROD}
	balena os configure ~/Downloads/balena-cloud-$${BALENA_OS_ARCH}-$${BALENA_OS_IMAGE_DEV}-${BALENA_OS_VERSION}.img --app $${APPLICATION}