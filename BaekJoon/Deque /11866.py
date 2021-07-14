import sys
from collections import deque


rotateQue = deque()
N, K = map(int, sys.stdin.readline().split())

for i in range(N):
    rotateQue.append(i+1)

A = "<"
for i in range(N):
    for j in range(K-1):
        rotateQue.append(rotateQue.popleft())
    num = rotateQue.popleft()
    A += str(num) + ", "

A =  A.rstrip(', ') + ">"
print(A)
