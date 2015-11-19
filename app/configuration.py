#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import json


def load():
    configuration = json.loads(os.environ.get('CONFIGURATION', '[]'))
    for c in configuration:
        c['unit'] = int(c['unit'])
        c['coils'] = [int(x) for x in c.get('coils', [])]
        c['discrete_inputs'] = [int(x) for x in c.get('discrete_inputs', [])]
        c['input_registers'] = [int(x) for x in c.get('input_registers', [])]
        c['holding_registers'] = [int(x) for x in c.get('holding_registers', [])]
    return configuration
