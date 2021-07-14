from collections import deque
import sys

def stackChecker(inputStr):
    stack = deque()
    for i in inputStr:
        if i =='(':
            stack.append(1)
        elif i =='[':
            stack.append(2)
        elif i ==')':
            if len(stack) == 0:
                return('no')
            else:
                if(1==stack[len(stack)-1]):
                    stack.pop()
                else :
                    return('no')
        elif i ==']':
            if len(stack) == 0:
                return('no')
            else:
                if(2==stack[len(stack)-1]):
                    stack.pop()
                else :
                    return('no')
        elif i=='.':
            if len(stack) == 0:
                return('yes')
            else :
                return('no') 

while(True):
    inputStr = sys.stdin.readline().rstrip()
    if (inputStr=='.'):
        break
    else:
        print(stackChecker(inputStr))


