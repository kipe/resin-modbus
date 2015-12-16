#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
import configuration


if __name__ == '__main__':
    configuration = configuration.load()

    mode = configuration.get('mode', '')

    if mode not in ['TCP_SLAVE', 'TCP_MASTER', 'RTU_SLAVE', 'RTU_MASTER']:
        sys.exit('Please set mode to either SLAVE or MASTER')

    if mode == 'TCP_SLAVE':
        from tcp_slave import main
    elif mode == 'TCP_MASTER':
        from tcp_master import main
    elif mode == 'RTU_SLAVE':
        from rtu_slave import main
    else:
        from rtu_master import main

    main()
