#! /usr/bin/env python
"""mapper.py"""

import sys


def perform_map():
    for line in sys.stdin:
        line = line.strip()
        t = tuple(i for i in line.split(','))
        lst = [t[1][:7], t[9], t[12]]
        for field in lst:
            print('%s\t%s\t%s' % (field, field, field))


if __name__ == '__main__':
    perform_map()
