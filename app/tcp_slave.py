#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import time
import random
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_tcp


def main():
    try:
        logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")

        server = modbus_tcp.TcpServer(address=os.environ.get('SLAVE_IP', '0.0.0.0'), port=int(os.environ.get('SLAVE_PORT', '5022')))
        server.start()

        slave = server.add_slave(1)
        slave.add_block('0', cst.HOLDING_REGISTERS, 0x321, 4)
        logger.info('Slave started.')

        while True:
            try:
                slave.set_values('0', 0x321, [
                    random.randrange(1390, 1400),
                    random.randrange(1390, 1400),
                    random.randrange(1390, 1400),
                    random.randrange(1390, 1400),
                ])
                time.sleep(1)
            except Exception as e:
                print(e)
                break
    finally:
        server.stop()
        logger.error('Slave stopped.')


if __name__ == '__main__':
    main()
