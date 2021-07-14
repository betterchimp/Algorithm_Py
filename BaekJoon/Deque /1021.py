import sys
from collections import deque


def One(Que):
    Que.popleft()
    return


def Two(Que):
    Que.append(Que.popleft())
    return


def Three(Que):
    Que.appendleft(Que.pop())
    return


def Check(que, numToFind):
    countTwo = 0
    countThree = 0
    while(que[0] != numToFind):
        Two(que)
        countTwo += 1
    for i in range(countTwo):
        Three(que)
    while(que[0] != numToFind):
        Three(que)
        countThree += 1
    for i in range(countThree):
        Two(que)
    if countTwo > countThree:
        while(que[0] != numToFind):
            Three(que)
        One(que)
        return 3, countThree
    while(que[0] != numToFind):
        Two(que)
    One(que)
    return 2, countTwo


rotateQue = deque()
Direction = 0
count = 0
N, G = map(int, sys.stdin.readline().split())
numToFind = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    rotateQue.append(i+1)

for i in range(G):
    thisCount = 0
    if(rotateQue[0] == numToFind[i]):
        One(rotateQue)
    else:
        Direction, thisCount = Check(rotateQue, numToFind[i])
    count += thisCount

print(count)

