FROM resin/armv7hf-debian:latest

RUN export DEBIAN_FRONTEND=noninteractive; apt-get update && apt-get install -y --force-yes python-serial python-pymodbus
