import sys
r = sys.stdin.readline
n, w = map(int, r().split())
wv = [list(map(int, r().split())) for _ in range(n)]
dp = [[0 for _ in range(w+1)] for __ in range(n+1)]
for i in range(n):
    for j in range(1, w+1):
        if wv[i][0] <= j:
            dp[i+1][j] = max(dp[i][j], dp[i][j-wv[i][0]] + wv[i][1])
        else:
            dp[i+1][j] = dp[i][j]
print(dp[n][w])
