#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os


def save(now, slave, coils, discrete_inputs, input_registers, holding_registers):
    target_file = '/data/modbus/slave_%i/%s' % (slave['unit'], now.strftime('%Y/%m/%d.txt'))
    target_path = os.path.dirname(target_file)

    if not os.path.exists(target_path):
        os.makedirs(target_path)
    if not os.path.exists(target_file):
        headers = ['datetime'] + \
            ['coil_%i' % x for x in slave['coils']] + \
            ['discrete_input_%i' % x for x in slave['discrete_inputs']] + \
            ['input_register_%i' % x for x in slave['input_registers']] + \
            ['holding_register_%i' % x for x in slave['holding_registers']]

        with open(target_file, 'a') as f:
            f.write('\t'.join(headers))
            f.write('\n')

    with open(target_file, 'a') as f:
        values = [now.strftime('%Y-%m-%d %H:%M:%S')] + \
            ['%i' % x for x in coils] + \
            ['%i' % x for x in discrete_inputs] + \
            ['%i' % x for x in input_registers] + \
            ['%i' % x for x in holding_registers]

        f.write('\t'.join(values))
        f.write('\n')
