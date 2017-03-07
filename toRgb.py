#!/usr/bin/env python

import sys

x = 0

for line in sys.stdin:
    x =  line.rstrip()

x = int(x, 16)
b = 0
b =  x & 0xFF

x = x >> 8
g = 0
g = x & 0xFF

x = x >> 8
r = 0
r = x & 0xFF

print("%d,%d,%d" % (r, g, b))
