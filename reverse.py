#!/usr/bin/env python

import sys

x = []

for line in sys.stdin:
    x.append(line.rstrip())

x.reverse()

for line in x:
    print(line)
