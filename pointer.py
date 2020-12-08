#!/usr/bin/env python3
from Xlib import display as d
import sys

while True:
    c = d.Display().screen().root.query_pointer()._data
    x = c["root_x"]
    y = c["root_y"]

    sys.stdout.write(f'{x:04} {y:04}\r')
    sys.stdout.flush()
