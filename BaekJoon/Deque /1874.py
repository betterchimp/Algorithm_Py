from collections import deque

stack = deque()
symbolStack = deque()

idx = 1
for i in range(int(input())):
    inputInt = int(input())
    while(True):
        if(len(stack) == 0):
            stack.append(idx)
            symbolStack.append("+")
            idx += 1
        elif(stack[len(stack)-1] == inputInt):
            stack.pop()
            symbolStack.append("-")
            break
        elif(stack[len(stack)-1] > inputInt):
            print('NO')
            quit()
        else:
            stack.append(idx)
            symbolStack.append("+")
            idx += 1

for i in range(len(symbolStack)):
    print(symbolStack.popleft())
