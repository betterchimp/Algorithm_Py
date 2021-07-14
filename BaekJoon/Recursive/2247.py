import sys
import math
from collections import deque

N = int(sys.stdin.readline())
result = ""
logN = int(math.log(N, 3))
quelist = list(range(logN))

def which(N, firstN):
    que = deque()
    if N == 1:
        return que
    for i in range(N//3, N//3*2):
        que.append(i)
    return que
'''
for i in range(logN):
    quelist[i] = which(N//(3**i), N)
'''
TF = True
for i in range(N):
    for j in range(N):
        TF = True
        '''
        for k in range(logN):
            if i in quelist[k] and j in quelist[k]:
                TF = False
        '''
        if TF:
            result += "*"
        else:
            result += " "
    result += "\n"
print(result)
