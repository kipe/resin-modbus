#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import time
import modbus_tk
from modbus_tk import modbus_tcp
import configuration
import slaves


def main():
    try:
        logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")

        master = modbus_tcp.TcpMaster(host=os.environ.get('SLAVE_IP', '0.0.0.0'), port=int(os.environ.get('SLAVE_PORT', '5022')))
        master.set_timeout(5.0)
        logger.info('Master connected.')

        config = configuration.load()

        while True:
            try:
                slaves.read(master, config.get('devices', []))
                time.sleep(1)
            except Exception as e:
                print(e)
                break
    finally:
        logger.error('Master stopped.')


if __name__ == '__main__':
    main()
