#!/usr/bin/env python3

n = int(input())

d = dict()

a = list(map(int, input().split()))
for x in a:
	if not x in d:
		d[x] = 0
	d[x] += 1

ans = 0
for x in d.keys():
	ans = max(ans, d[x])

print(ans)