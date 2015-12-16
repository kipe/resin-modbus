#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import json

CONFIG_FILE = '/data/modbus/configuration.json'


def load():
    configuration = {}
    if not os.path.exists(CONFIG_FILE):
        return configuration

    with open(CONFIG_FILE, 'r') as f:
        configuration = json.loads(f.read())
    return configuration
