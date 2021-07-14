import sys
import math
T = int(sys.stdin.readline())
distance = list(range(T))
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    distance[i] = b-a

def fun_2(a,b,c):
    return ((-b+math.sqrt(b**2-4*a*c))/2*a, (-b-math.sqrt(b**2-4*a*c))/2*a)
count = 0
for i in range(T):
    a, b = map(int, fun_2(1,1,-distance[i]))
    c, d = map(int, fun_2(1,2,-distance[i]+1))
    #print("a :",a)
    #print("c :",c)
    if a > c :
        count = 2*a + math.ceil((distance[i] - (a**2+a)) / a)
    else :
        count = 2*c + 1 + math.ceil((distance[i] - ((c**2+c)+c+1)) / (c+1))
    print(count)