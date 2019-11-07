#!/usr/bin/env python3.7

from random import randint, choice, shuffle

last_test = 1
MAXN = 10 ** 5
MAXA = 10 ** 9

def gen_1_batch():
    global last_test
    with open("tests/%03d" % last_test, 'w') as f:
        last_test += 1
        n = randint(0, MAXN)
        f.write(f'{n}\n')
        arr = [randint(0, MAXA) for i in range(n)]
        while len(set(arr)) != n:
            arr = [randint(1, MAXA) for i in range(n)]
        f.write(' '.join([str(x) for x in arr]) + '\n')


def gen_2_batch():
    global last_test
    with open("tests/%03d" % last_test, 'w') as f:
        last_test += 1
        n_diff = randint(1, int(MAXN ** 0.5))
        n_each = randint(1, int(MAXN ** 0.5))
        n = n_diff * n_each
        f.write(f'{n}\n')
        arr = []
        for _ in range(n_diff):
            arr.extend([randint(0, MAXA)] * n_each)
        shuffle(arr)
        f.write(' '.join([str(x) for x in arr]) + '\n')


def gen_3_batch():
    global last_test
    with open("tests/%03d" % last_test, 'w') as f:
        last_test += 1
        n = randint(0, MAXN)
        f.write(f'{n}\n')
        arr = [randint(1, 2) for _ in range(n)]
        f.write(' '.join([str(x) for x in arr]) + '\n')
        

def gen_4_batch():
    global last_test
    with open("tests/%03d" % last_test, 'w') as f:
        last_test += 1
        l = randint(0, MAXA)
        r = randint(l, min(MAXA, l + 1000))
        n = randint(0, 1000)
        f.write(f'{n}\n')
        arr = [randint(l, r) for _ in range(n)]
        f.write(' '.join([str(x) for x in arr]) + '\n')


def gen_5_batch():
    global last_test
    with open("tests/%03d" % last_test, 'w') as f:
        last_test += 1
        l = randint(0, MAXA)
        r = randint(l, min(MAXA, l + 1000))
        n = randint(0, MAXN)
        f.write(f'{n}\n')
        arr = [randint(l, r) for _ in range(n)]
        f.write(' '.join([str(x) for x in arr]) + '\n')


def main():
    for _ in range(10):
        print(f'Creating test {last_test}')
        gen_1_batch()
    for _ in range(15):
        print(f'Creating test {last_test}')
        gen_2_batch()
    for _ in range(15):
        print(f'Creating test {last_test}')
        gen_3_batch()
    for _ in range(30):
        print(f'Creating test {last_test}')
        gen_4_batch() 
    for _ in range(30):
        print(f'Creating test {last_test}')
        gen_5_batch()


if __name__ == '__main__':
    main()
