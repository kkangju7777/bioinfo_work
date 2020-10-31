#!/bin/usr/env python3

import sys

def FASTQparse(file_name):
    cnt = 0
    with open(file_name,'r') as handle:
        for line in handle:
            cnt +=1
    return cnt

if len(sys.argv) != 2:
    print(f'#usage: python {sys.argv[0]} [fastq]')
    sys.exit()

file_name = sys.argv[1]
cnt = FASTQparse(file_name)
print(cnt/4)


