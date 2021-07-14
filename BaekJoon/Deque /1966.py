import sys
from collections import deque

#한바퀴 둘러서 최대값 
def checkMaxImp(que):
    max = -1
    for i in range(len(que)):
        if max < que[0]:
            max = que[0]
        que.append(que.popleft())
    return max

numQueue = deque()
priorQueue = deque()
T = int(sys.stdin.readline())
for i in range(T):
    N, numFind = map(int, sys.stdin.readline().split())
    impList = list(map(int, sys.stdin.readline().split()))

    for i in range(N):
        numQueue.append(i)
    for i in impList:
        priorQueue.append(i)
        
    numOut = -1
    count = 0
    while(True):
        if priorQueue[0] == checkMaxImp(priorQueue):
            numOut = numQueue.popleft()
            priorQueue.popleft()
            count += 1
        else:
            numQueue.append(numQueue.popleft())
            priorQueue.append(priorQueue.popleft())
        if(numOut == numFind):
            break;
    print(count)
    numQueue.clear()
    priorQueue.clear()