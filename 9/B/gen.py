#!/usr/bin/env python3.7

from random import randint, choice

last_test = 1
MAXN = 10 ** 9

def gen_test(l, r):
    global last_test
    with open("tests/%03d" % last_test, 'w') as f:
        last_test += 1
        cur_l = randint(l, r)
        cur_r = randint(l, r)
        cur_l, cur_r = min(cur_l, cur_r), max(cur_l, cur_r)
        f.write(f'{cur_l} {cur_r}\n')



def main():
    for _ in range(10):
        gen_test(0, 10)
    for _ in range(30):
        x = randint(0, MAXN)
        gen_test(x, x)
    for _ in range(30):
        gen_test(0, 1000)
    for _ in range(30):
        gen_test(0, MAXN)


if __name__ == '__main__':
    main()
