#!/usr/bin/env python3.7

from random import randint, choice

last_test = 1

def gen_test(char):
    global last_test
    with open("tests/%03d" % last_test, 'w') as f:
        last_test += 1
        f.write(char + '\n')


def main():
    for c in range(ord('A'), ord('Z') + 1):
        gen_test(chr(c))

if __name__ == '__main__':
    main()
