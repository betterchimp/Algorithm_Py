import sys
from collections import deque

dequeA = deque()
T = int(sys.stdin.readline())
N= 0
P = ""
condition = 0
error = 0
answer = "["
for i in range(T):
    answer = "["
    condition = 0
    P = sys.stdin.readline()
    N = int(sys.stdin.readline())
    if N == 0:
        sys.stdin.readline()
    else :
        for j in list(map(int, sys.stdin.readline().rstrip(']\n').lstrip('[').split(','))):
            dequeA.append(j)
    for i in P:
        if i =='R':
            if condition == 0:
                condition = 1
            else : #if cond == 1
                condition = 0
        elif i=='D':
            if len(dequeA) == 0:
                print('error')
                error = 1
                break
            if condition == 0:
                dequeA.popleft()
            else :
                dequeA.pop()
    if error==0:
        for i in range(len(dequeA)):
            if condition == 0:
                answer += str(dequeA.popleft())+","
            else :
                answer += str(dequeA.pop())+","
        print(answer.rstrip(',')+"]")
        error==0
    else :
        error=0
    dequeA.clear()