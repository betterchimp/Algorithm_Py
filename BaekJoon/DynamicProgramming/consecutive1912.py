import sys
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
dp = [0 for i in range(n)]
dp[0] = s[0]
for i in range(n):
    dp[i] = max(s[i], s[i] + dp[i - 1])
print(max(dp))