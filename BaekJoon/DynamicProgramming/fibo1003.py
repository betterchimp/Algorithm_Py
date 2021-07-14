import sys


def zerOne(n):
    if n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    else:
        for i in range(2, n+1):
            lst[i] = [lst[i-1][0] + lst[i-2][0], lst[i-1][1] + lst[i-2][1]]
        return lst[n]


T = int(sys.stdin.readline())
lst = [[1, 0], [0, 1]]
for i in range(39):
    lst.append([0, 0])
for i in range(T):
    result = zerOne(int(sys.stdin.readline()))
    print("%d %d" % (result[0], result[1]))
