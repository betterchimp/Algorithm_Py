import sys, copy
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
dp = [1 for i in range(n)]
temp = [[] for i in range(n)]
maxIdx = 0
maxVal = 1
for i in range(n):
    for j in range(i):
        if s[i] > s[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
            temp[i] = copy.deepcopy(temp[j])
    temp[i].append(s[i])
    if dp[i] > maxVal:
        maxIdx = i
        maxVal = dp[i]

print(maxVal)
print(' '.join(map(str, temp[maxIdx])))
