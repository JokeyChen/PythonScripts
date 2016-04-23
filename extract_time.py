#!/usr/bin/python
import re
from sys import argv

def main():
    body = ''
    if len(argv) - 1 != 1:
        print 'argv incorrect!'
    else:
        with open(argv[1], 'r') as f:
            body = f.read()
        # now parse the inputfile
        time_list = re.findall(r'?\d\.\d\d', body)
        with open(argv[1], 'w') as f:
            for time in time_list:
                f.write(time + '\n')

if __name__ == '__main__':
    main()
