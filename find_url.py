#!/usr/bin/env python

import re
import sys

for i in re.findall('<a href="?\'?([^"\'>]*)', open(sys.argv[1], 'r').read()):
    print i
