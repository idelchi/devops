FROM python:3.10-slim

LABEL project=unnamed \
    maintainer=arash.idelchi@gmail.com

USER root

ARG DEBIAN_FRONTEND=noninteractive

RUN pip install --no-cache-dir \
    requests \
    flask \
    pyopenssl

# Create CI User (Debian/Ubuntu)
RUN groupadd -r -g 1000 ci && \
    useradd -r -u 1000 -g 1000 -m -c "ci account" -d /home/ci -s /bin/bash ci

USER ci
WORKDIR /home/ci

COPY main.py main.py
COPY *.pem ./

ENV TZ=Europe/Zurich
