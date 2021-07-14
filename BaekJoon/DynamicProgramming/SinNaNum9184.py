import sys
dp = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]


def w(a, b, c):
    if a < 1 or b < 1 or c < 1:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return 1048576
    elif dp[a][b][c] > 0:
        return dp[a][b][c]
    else:
        if a < b and b < c:
            dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return dp[a][b][c]
        else:
            dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return dp[a][b][c]


while(True):
    a, b, c = map(int, (sys.stdin.readline().split()))
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))
