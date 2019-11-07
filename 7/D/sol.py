#!/usr/bin/env python3

s = input()
n = len(s)

a = [0] * 6

su = 0
for x in s:
	a[int(x)] += 1
	su += int(x)

i = 1
ans = 0
while su / n < 3.5:
	if a[i]:
		a[i] -= 1
		su += 5 - i
		ans += 1
	else:
		i += 1

print(ans)