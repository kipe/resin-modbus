#!/bin/sh
apt-get update && apt-get install -y --force-yes python-pip python-dev git-core supervisor
pip install -U pip
mkdir -p /data/modbus
git clone https://github.com/kipe/resin-modbus.git ~/resin-modbus
ln -s ~/resin-modbus/app /app
cp ~/resin-modbus/configuration_example.json /data/modbus/configuration.json
/usr/local/bin/pip install -r /app/requirements.txt
ln -s /app/supervisor.conf /etc/supervisor/conf.d/modbus.conf
service supervisor restart
