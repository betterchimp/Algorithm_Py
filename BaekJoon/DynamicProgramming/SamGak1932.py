import sys, copy
N = int(sys.stdin.readline())
temp = [0]
for i in range(N):
    dp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(dp)):
        if j == 0:
            dp[j] = temp[j] + dp[j]
        elif j == len(dp)-1:
            dp[j] = temp[j-1] + dp[j]
        else:
             dp[j] = max(temp[j-1], temp[j]) + dp[j]
    temp = copy.deepcopy(dp)
print(max(dp))
