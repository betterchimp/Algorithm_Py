import sys

count = 0
num = 666
N = int(sys.stdin.readline())

lst = list(range(N+1))
while(count < N):
    if "666" in str(num):
        count += 1
        lst[count] = num
    num += 1

print(num -1)
