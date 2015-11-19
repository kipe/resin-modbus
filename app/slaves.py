#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from datetime import datetime
import modbus_tk.defines as cst
import configuration
import log


def create(server, logger=None):
    for s in configuration.load():
        slave = server.add_slave(s['unit'])
        for x in s['coils']:
            block_name = 'unit_%i_coil_%i' % (s['unit'], x)
            slave.add_block(block_name, cst.COILS, x, 1)
            slave.set_values(block_name, x, True)
        for x in s['discrete_inputs']:
            block_name = 'unit_%i_discrete_input_%i' % (s['unit'], x)
            slave.add_block(block_name, cst.DISCRETE_INPUTS, x, 1)
            slave.set_values(block_name, x, True)
        for x in s['input_registers']:
            block_name = 'unit_%i_input_register_%i' % (s['unit'], x)
            slave.add_block(block_name, cst.HOLDING_REGISTERS, x, 1)
            slave.set_values(block_name, x, x)
        for x in s['holding_registers']:
            block_name = 'unit_%i_holding_register_%i' % (s['unit'], x)
            slave.add_block(block_name, cst.HOLDING_REGISTERS, x, 1)
            slave.set_values(block_name, x, x)

        if logger is not None:
            logger.info('Slave unit %i added.' % (s['unit']))


def read(master, config):
    for s in config:
        now = datetime.utcnow()
        coils = [
            master.execute(s['unit'], cst.READ_COILS, x, 1)[0]
            for x in s['coils']
        ]
        discrete_inputs = [
            master.execute(s['unit'], cst.READ_DISCRETE_INPUTS, x, 1)[0]
            for x in s['discrete_inputs']
        ]
        input_registers = [
            master.execute(s['unit'], cst.READ_INPUT_REGISTERS, x, 1)[0]
            for x in s['input_registers']
        ]
        holding_registers = [
            master.execute(s['unit'], cst.READ_HOLDING_REGISTERS, x, 1)[0]
            for x in s['holding_registers']
        ]
        log.save(now, s, coils, discrete_inputs, input_registers, holding_registers)
