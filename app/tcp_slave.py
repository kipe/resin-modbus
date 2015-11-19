#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import time
import modbus_tk
from modbus_tk import modbus_tcp
import slaves


def main():
    try:
        logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")

        server = modbus_tcp.TcpServer(address=os.environ.get('SLAVE_IP', '0.0.0.0'), port=int(os.environ.get('SLAVE_PORT', '5022')))
        server.start()
        slaves.create(server, logger)

        while True:
            try:
                time.sleep(1)
            except Exception as e:
                print(e)
                break
    finally:
        server.stop()
        logger.error('Slave stopped.')


if __name__ == '__main__':
    main()
