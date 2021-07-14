import sys
import copy
N = int(sys.stdin.readline())
f = [0] + [1 for i in range(9)]
sum = 0
for length in range(N-1):
    s = [0 for i in range(10)]
    for numIdx in range(10):
        if numIdx < 1:
            s[numIdx+1] += f[numIdx]
        elif numIdx < 9:
            s[numIdx+1] += f[numIdx]
            s[numIdx-1] += f[numIdx]
        else:
            s[numIdx-1] += f[numIdx]
    f = copy.deepcopy(s)
for i in range(10):
    sum += f[i]
print(sum % (10**9))