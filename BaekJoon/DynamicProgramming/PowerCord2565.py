import sys
n = int(sys.stdin.readline())
el = [[] for i in range(n)]
dp = [1 for i in range(n)]
for i in range(n):
    el[i] = list(map(int, sys.stdin.readline().split()))
el.sort()
for i in range(n):
    for j in range(i):
        if el[i][1] > el[j][1] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
print(n-max(dp))


