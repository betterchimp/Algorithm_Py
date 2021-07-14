import sys
# from collections import deque

N, M = map(int, sys.stdin.readline().split())

chessTable = []
for i in range(N):
    chessTable.append(sys.stdin.readline())
minimum = 64
for verStep in range(N-7):
    for horStep in range(M-7):
        countW = 0
        countB = 0
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 1:
                    if chessTable[i+verStep][j+horStep] == 'W':
                        countW += 1
                    else:
                        countB += 1
                else:
                    if chessTable[i+verStep][j+horStep] == 'B':
                        countW += 1
                    else:
                        countB += 1
        if countW > countB:
            if minimum > countB:
                minimum = countB
        else:
            if minimum > countW:
                minimum = countW
print(minimum)
