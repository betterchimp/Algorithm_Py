import sys
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
lengthA = len(a)
lengthB = len(b)
dp = [0 for i in range(lengthA)]
pos = [0 for i in range(lengthA)]

for i in range(lengthA):
    for j in range(lengthB):
        if a[i] == b[j]:
            dp[i] = 1
            pos[i] = j
            break
    for k in range(i):
        for l in range(pos[k] + 1, len(b)):
            if b[l] == a[i]:
                if dp[i] <= dp[k]:
                    dp[i] = dp[k] + 1
                    pos[i] = l
                break
print(max(dp))