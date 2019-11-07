#!/usr/bin/env python3.7

from random import randint, choice

last_test = 1
MAXN = 10 ** 5

def gen_test(n, diff):
    global last_test
    with open("tests/%03d" % last_test, 'w') as f:
        last_test += 1
        ch = [randint(0, 2) for i in range(diff)]
        f.write(''.join([str(choice(ch)) for i in range(n)]) + '\n')


def main():
    for _ in range(20):
        gen_test(2, randint(1, 2))
    for _ in range(20):
        gen_test(3, randint(1, 3))
    for _ in range(60):
        gen_test(randint(0, MAXN), randint(1, 3))

if __name__ == '__main__':
    main()
