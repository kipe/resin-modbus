FROM resin/armv7hf-debian:latest

RUN export DEBIAN_FRONTEND=noninteractive; apt-get update && apt-get install -y --force-yes dropbear python-pip python-dev
RUN pip install -U pip
ADD app /app
RUN pip install -r /app/requirements.txt
RUN chmod a+x /app/start.sh

CMD /app/start.sh
