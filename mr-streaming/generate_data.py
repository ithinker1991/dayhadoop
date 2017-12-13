
import random


key = []

for i in range(5):
    l = random.randint(1, 10)
    r = random.randint(1, 10)
    print '%s\tJAVA%s' % (chr(l % 26 + ord('a')), r)
    key.append(chr(l % 26 + ord('a')))

for k in key:
    r = random.randint(20, 30)
    print "%s\tHADOOP%s" % (k, r)
