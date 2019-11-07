#!/usr/bin/env python3.7

from random import randint, choice, shuffle

last_test = 1
MAXN = 10 ** 5


def add_trash(s, deg):
    for _ in range(deg):
        s[randint(0, len(s) - 1)] = choice([':', '|'])


def gen_1_batch():
    global last_test
    with open("tests/%03d" % last_test, 'w') as f:
        last_test += 1
        n = randint(0, MAXN)
        pairity = randint(0, 1)
        f.write(''.join([':' if i % 2 == pairity else '|' for i in range(n)]) + '\n')


def gen_2_batch():
    global last_test
    with open("tests/%03d" % last_test, 'w') as f:
        last_test += 1
        n = randint(1, 13)
        s = []
        while len(s) < n:
            s.extend(choice([list(':|'), list('|:'), list('|:|')]))
        add_trash(s, randint(0, int(len(s) / 10)))
        f.write(''.join(s))


def gen_3_batch():
    global last_test
    with open("tests/%03d" % last_test, 'w') as f:
        last_test += 1
        n = randint(1, MAXN - 2)
        s = []
        while len(s) < n:
            s.extend(choice([list(':|'), list('|:'), list('|:|')]))
        add_trash(s, randint(0, int(len(s) / 10)))
        f.write(''.join(s))


def main():
    for _ in range(30):
        print(f'Creating test {last_test}')
        gen_1_batch()
    for _ in range(30):
        print(f'Creating test {last_test}')
        gen_2_batch()
    for _ in range(40):
        print(f'Creating test {last_test}')
        gen_3_batch()


if __name__ == '__main__':
    main()
