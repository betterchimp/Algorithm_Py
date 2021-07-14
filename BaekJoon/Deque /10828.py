'''
・ 완전 일치 : == , !=

・ 부분 일치 : in , not in

・ 전방 일치 : startswith()

・ 후방 일치 : endswith()
'''
from collections import deque
import sys


stack = deque()
for i in range(int(input())):
    order = sys.stdin.readline().rstrip()
    if(order.startswith('push')):
        a, b = order.split()
        stack.append(b)
    elif(order.startswith('pop')):
        if len(stack) == 0:
            print(-1)
        else :
            print(stack.pop())
    elif(order.startswith('size')):
        print(len(stack))
    elif(order.startswith('empty')):
        if len(stack) == 0:
            print(1)
        else :
            print(0)
    elif(order.startswith('top')):
        if len(stack) == 0:
            print(-1)
        else :
            print(stack[len(stack)-1])
    else:
        print()

