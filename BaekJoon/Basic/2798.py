import sys

N, M = map(int,sys.stdin.readline().split())
lst= list(map(int, list(sys.stdin.readline().split()))) 
max = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if (M - max) > (M-(lst[i]+lst[j]+lst[k])) and (M-(lst[i]+lst[j]+lst[k])) > -1 and i !=k and k!=j and i!=j :
                max = lst[i]+lst[j]+lst[k]
print(max)