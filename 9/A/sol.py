#!/usr/bin/env python3

a = input()

n = ord(a) - ord('A') + 1

lst = [0] * n
lst[0] = 1
for x in range(1, n):
	lst[x] = 2 * lst[x - 1] + 1

print(lst[n - 1])