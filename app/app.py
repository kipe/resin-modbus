#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import sys


if __name__ == '__main__':
    MODE = os.environ.get('MODE', '').strip()

    if MODE not in ['TCP_SLAVE', 'TCP_MASTER', 'RTU_SLAVE', 'RTU_MASTER']:
        sys.exit('Please set MODE to either SLAVE or MASTER')

    if MODE == 'TCP_SLAVE':
        from tcp_slave import main
    elif MODE == 'TCP_MASTER':
        from tcp_master import main
    elif MODE == 'RTU_SLAVE':
        from rtu_slave import main
    else:
        from rtu_master import main

    main()
