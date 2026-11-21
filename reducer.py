#!/usr/bin/env python
"""reducer.py"""
from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    counts = []
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            counts.append((current_word, total_count))
        except ValueError:
            pass

    top_three = sorted(counts, key=itemgetter(1), reverse=True)[:3]
    for word, total_count in top_three:
        print ("%s%s%d" % (word, separator, total_count))

if __name__ == "__main__":
    main()
