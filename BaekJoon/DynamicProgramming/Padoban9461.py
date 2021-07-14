import sys

def P(N):
    if N < 4:
        return 1
    elif N < 6:
        return 2
    else:
        if DP[N] > 0:
            return DP[N]
        else:
            DP[N] = P(N-1) + P(N-5)
        return DP[N]

DP = [0] * 101
T = int(sys.stdin.readline())
for i in range(T):
    print(P(int(sys.stdin.readline())))