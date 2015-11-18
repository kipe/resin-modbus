#!/bin/sh
apt-get update && apt-get install -y --force-yes python-pip python-dev git-core
pip install -U pip
mkdir /data
git clone https://github.com/kipe/resin-modbus.git ~/resin-modbus
ln -s ~/resin-modbus/app /app
/usr/local/bin/pip install -r /app/requirements.txt
