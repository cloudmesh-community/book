FROM mongo:4.2.0-bionic

RUN set -x \
        && apt-get update \
        && apt-get install -y \
            python3 \
            python3-pip \
            python3-venv \
        && rm -rf /var/lib/apt/lists/* \
        && update-alternatives --install /usr/bin/python python /usr/bin/python3 1

EXPOSE 27017