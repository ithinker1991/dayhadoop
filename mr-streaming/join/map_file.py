
import sys

# python 0  ;map_file 1  1; 1 2
arg = sys.argv[2]

for line in sys.stdin:
    v1, v2 = line.strip().split()

    print '\t'.join([v1, arg, v2])


