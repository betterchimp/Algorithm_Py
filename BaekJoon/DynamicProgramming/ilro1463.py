import sys
N = int(sys.stdin.readline())
DP = [0 for i in range(N+1)]
for i in range(2, N+1):
    DP[i] = DP[i-1] + 1
    if i % 3 == 0:
        DP[i] = min(DP[i//3] + 1, DP[i])
    if i % 2 == 0:
        DP[i] = min(DP[i//2] + 1, DP[i])
print(DP[N])

'''
def X(n):
    if n < 2 :
        return 0
    if n < 4 :
        return 1
    if n % 3 == 0:
        return X(n//3) + 1
    elif n % 2 == 0:
        return min(X(n//2), X(n-1)) + 1
    else:
        return X(n-1) + 1
'''