#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import json
import configuration

os.environ['CONFIGURATION'] = '''
[
    {
        "unit": 1,
        "coils": [1, 2, 74, 89],
        "holding_registers": [801, 802, 803, 804]
    }
]
'''

print(configuration.load())
print(json.dumps(configuration.load()).replace(' ', ''))
