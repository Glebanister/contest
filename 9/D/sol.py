#!/usr/bin/env python3

s = input()
s = s[::-1]

n = len(s)
dp = [-10**9] * (n + 1)
dp[0] = 0

for x in range(0, n - 1):
	if dp[x] >= 0:
		if s[x] == '|' and s[x + 1] == ':':
			dp[x + 2] = max(dp[x + 2], dp[x] + 1)
		if s[x] == ':' and s[x + 1] == '|':
			dp[x + 2] = max(dp[x + 2], dp[x])
		if x < n - 2 and s[x] == '|' and s[x + 1] == ':' and s[x + 2] == '|':
			dp[x + 3] = max(dp[x + 3], dp[x])
print(max(dp))