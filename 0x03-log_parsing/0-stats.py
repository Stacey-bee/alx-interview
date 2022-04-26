#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''


import re
import sys


def magicComputer():
    ''' this function is called to do the
        work specified in the comment above
    '''
    regex = r'^((?:[0-9]{1,3}\.){3}[0-9]{1,3}) - (\[.+\]) "GET \/projects\/260 HTTP\/1.1" (\d+) (\d+)'
    lines = sys.stdin.readlines()
    cache = {'200': 0, '301': 0, '400': 0, '401': 0,
             '403': 0, '404': 0, '405': 0, '500': 0}
    total_size = 0
    counter = 0

    try:
        for line in lines:
            if re.match(regex, line):
                counter += 1
                res = re.search(regex, line)
                total_size += int(res.group(4))
                cache[res.group(3)] += 1

            if counter >= 10:
                counter = 0
                print('File size: {}'.format(total_size))
                total_size = 0
                for key, value in sorted(cache.items()):
                    if value != 0:
                        print('{}: {}'.format(key, value))
                        cache[key] = 0

    except Exception as err:
        print('File size: {}'.format(total_size))
        total_size = 0
        for key, value in sorted(cache.items()):
            if value != 0:
                print('{}: {}'.format(key, value))
        raise err

    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

if __name__ == '__main__':
    magicComputer()
