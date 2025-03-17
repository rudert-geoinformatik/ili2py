FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y \
        openjdk-21-jre \
        curl \
        unzip \
        make

# install & setup ili2c
ARG ILI2C_VERSION=5.6.3
RUN curl -o /tmp/ili2c-${ILI2C_VERSION}.zip https://downloads.interlis.ch/ili2c/ili2c-${ILI2C_VERSION}.zip && \
  rm -rf /tmp/ili2c && \
  mkdir /tmp/ili2c && \
  unzip -d /ili2c /tmp/ili2c-${ILI2C_VERSION}.zip && \
  chmod -R ogu+rwx /ili2c/* && \
  echo "#!/usr/bin/env bash" > /usr/bin/ili2c && \
  echo "java -jar /ili2c/ili2c.jar \$@" >> /usr/bin/ili2c && \
  chmod +x /usr/bin/ili2c && \
  echo "alias ili2c='/usr/bin/ili2c'" >> /root/.bashrc

ADD . /io

ENTRYPOINT ["make"]

WORKDIR /io
