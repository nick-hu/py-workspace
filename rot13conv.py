#!/usr/bin/python

import sys
import re

old, new = open(sys.argv[1]), open(sys.argv[2], 'w')

new.writelines(['#!/usr/bin/python\n', '# -*- coding: rot13 -*-\n'])
print '# -*- coding: rot13 -*-\n'
for line in old:
    if not line.startswith('#!'):
        find = re.findall(r"'[\s\S]*'", line)
        print find
        for i in find:
            line = line.replace(i, 'u' + i)
        print line
        new.write(line.encode('rot13'))

old.close()
new.close()
