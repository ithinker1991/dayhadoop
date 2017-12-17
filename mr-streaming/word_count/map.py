#!/usr/local/bin/python


import sys


def reduce():
    last_word = None
    last_sum = 0

    for line in sys.stdin:

        word, val = line.strip().split()

        if last_word == None:
            last_word = word

        if last_word == word:
            last_sum += int(val)

        else:
            print '%s\t%s' % (last_word, last_sum)
            last_sum = int(val)
            last_word = word

    print '%s\t%s' % (last_word, last_sum)


def reduer_func():
    current_word = None
    count_pool = []
    sum = 0

    for line in sys.stdin:
        word, val = line.strip().split()

        if current_word == None:
            current_word = word

        if current_word != word:
            for count in count_pool:
                sum += count
            print "%s\t%s" % (current_word, sum)
            current_word = word
            count_pool = []
            sum = 0

        count_pool.append(int(val))

    for count in count_pool:
        sum += count
    print "%s\t%s" % (current_word, str(sum))


if __name__ == '__main__':
    # reduce()
    reduer_func()