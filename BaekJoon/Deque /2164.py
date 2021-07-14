import sys
from collections import deque


rotateQue = deque()
N = int(sys.stdin.readline())

for i in range(N):
    rotateQue.append(i+1)

rotateQue.appendleft(rotateQue.pop())
while(len(rotateQue)>0):
    rotateQue.append(rotateQue.popleft())
    num = rotateQue.popleft()
print(num)
