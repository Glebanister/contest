#!/usr/bin/env python3.7

import os

def main():
    os.system('rm -rf tests')
    os.system('mkdir -p tests')
    print('Generating tests...')
    os.system('python3 gen.py')
    for filename in os.listdir('tests/'):
        print(f'Getting answer on test {filename}')
        os.system(f'python3 sol.py < tests/{filename} > tests/{filename}.a')

if __name__ == '__main__':
    main()