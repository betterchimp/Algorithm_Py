import sys
from collections import deque

stackN = deque()
stackComp = deque()
stackTemp = deque()
sys.stdin.readline()

for i in list(map(int, sys.stdin.readline().split())):
    stackN.appendleft(i)
length = len(stackN)
lst = list(range(length))
stackComp.appendleft(-1)
idx = length -1
while(idx > -1):
    if (stackComp[0] > stackN[0]) or (stackComp[0] == -1):
        lst[idx] = stackComp[0]
        stackComp.appendleft(stackN.popleft())
    else:
        stackTemp = stackComp
        stackComp.popleft()
        while(True):
            if(stackComp[0] > stackN[0] or stackComp[0] == -1):
                lst[idx] = stackComp[0]
                stackComp.appendleft(stackN.popleft())
                break
            else:
                stackComp.popleft()
        stackComp = stackTemp
    idx -= 1
result =""
for i in lst:
    result += str(i)+" "
print(result)


'''
import sys

def NEG(lst, position, length, itself):
    idx = 1
    while(True):
        if(length < (position+idx)):
            return "-1"
        elif(itself < lst[position+idx-1]):
            return str(lst[position+idx-1])
        else:
            idx +=1
            
sys.stdin.readline()
llst = sys.stdin.readline().split()
lst = list(map(int, llst))

length = len(lst)
A = ""
for i in range(length-1):
    A += (NEG(lst, i+1, length, int(lst[i])) + " ")
print(A + "-1")
'''