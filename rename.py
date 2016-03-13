#!/usr/bin/python
import os
import re

suffix = 'pdf'
new_name_prefix = 'CSE140 Lecture '
for file in os.listdir('.'):
    if file[len(file) - len(suffix) : len(file)] == suffix:
        day = re.search(r'\d+', file).group(0)
        new_name = new_name_prefix + day + '.' + suffix
        os.rename(file, new_name)
