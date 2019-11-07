#!/usr/bin/env python3

a, b = map(int, input().split())

if a == 0:
	print(0)
	exit()

a = bin(a)
b = bin(b)

if len(a) != len(b):
	print(1)
else:
	ans = 0
	for x in range(2, len(a)):
		if a[x] != b[x]:
			break
		else:
			ans += 1
	print(ans)