import sys
from collections import deque


stack = deque()
    order = sys.stdin.readline().rstrip()
    if(order.startswith('push_f')):
        a, b = order.split()
        stack.appendleft(b)
    elif(order.startswith('push_b')):
        a, b = order.split()
        stack.append(b)
    elif(order.startswith('pop_f')):
        if len(stack) == 0:
            print(-1)
        else :
            print(stack.popleft())
    elif(order.startswith('pop_b')):
        if len(stack) == 0:
            print(-1)
        else :
            print(stack.pop())
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
