#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import sys


if __name__ == '__main__':
    MODE = os.environ.get('MODE', '').strip()

    if MODE not in ['SLAVE', 'MASTER']:
        sys.exit('Please set MODE to either SLAVE or MASTER')

    if MODE == 'SLAVE':
        from tcp_slave import main
    else:
        from tcp_master import main

    main()
