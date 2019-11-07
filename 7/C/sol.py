#!/usr/bin/env python3.7

s = input()
n = len(s)

a = [0] * 3

for x in s:
	a[int(x)] += 1

if a[0] > 0 and a[1] > 0 and a[2] > 0:
	print(0)
elif a[0] == n or a[1] == n or a[2] == n:
	print(0)
else:
	for x in range(3):
		for y in range(x + 1, 3):
			if a[x] > 0 and a[y] > 0 and y - x == 1:
				print(a[y])
			if a[x] > 0 and a[y] > 0 and y - x == 2:
				print(a[x])