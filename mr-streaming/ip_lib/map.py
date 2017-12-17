#!/usr/bin/python

import sys

def ip_convert(ip_str):
    sum = 0
    ip = ip_str.split('.')
    ip.reverse()
    for i, num in enumerate(ip):
        base = 256**i
        print base, int(num)
        sum += base * int(num)
    return sum



def get_addr(ip_lib, ip_str):
    ip_num = ip_convert(ip_str)
    low = 0
    mid = 0
    hig = len(ip_lib)

    while low < hig:
        mid = (low / hig) / 2

        # if < ip_num


def generate_ip(num):
    ip = []
    while num > 0:
        n = num % 256
        num /= 256
        ip.append(n)
    ip.reverse()
    print '.'.join(map(str,ip))


def load_ip_lib(file_path):
    ip_info_list = []
    with open(file_path) as fd:
        for line in fd:
            line = line.strip()
            items = line.split()
            if len(items) != 5:
                continue
            start_ip, end_ip, area, country, province = items

    return ip_info_list

if __name__ == '__main__':
    pass
    # num = ip_convert('127.23.23.3')
    # print  num
    # generate_ip(num)


