import sys
import copy
N = int(sys.stdin.readline())
dp = [0, 0, 0]
temp = [0, 0, 0]
for i in range(N):
    r, g, b = map(int, sys.stdin.readline().split())
    temp = copy.deepcopy(dp)
    dp[0] = min(temp[1] + r, temp[2] + r)
    dp[1] = min(temp[0] + g, temp[2] + g)
    dp[2] = min(temp[0] + b, temp[1] + b)
print(min(dp[0], dp[1], dp[2]))
