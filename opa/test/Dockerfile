FROM python:3.10

LABEL project=unnamed \
    maintainer=arash.idelchi@gmail.com

USER root

ARG DEBIAN_FRONTEND=noninteractive

RUN pip install --no-cache-dir \
    requests \
    pytest

# Create CI User (Debian/Ubuntu)
RUN groupadd -r -g 1000 ci && \
    useradd -r -u 1000 -g 1000 -m -c "ci account" -d /home/ci -s /bin/bash ci

USER ci
WORKDIR /home/ci

ENV TZ=Europe/Zurich
