import sys
from collections import deque


stack = deque()
for i in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().rstrip()
    if(order.startswith('pu')):
        a, b = order.split()
        stack.append(b)
    elif(order.startswith('po')):
        if len(stack) == 0:
            print(-1)
        else :
            print(stack.popleft())
    elif(order.startswith('s')):
        print(len(stack))
    elif(order.startswith('e')):
        if len(stack) == 0:
            print(1)
        else :
            print(0)
    elif(order.startswith('f')):
        if len(stack) == 0:
            print(-1)
        else :
            print(stack[0])
    elif(order.startswith('b')):
        if len(stack) == 0:
            print(-1)
        else :
            print(stack[len(stack)-1])
