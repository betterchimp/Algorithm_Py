import sys
N = sys.stdin.readline().rstrip()
t = len(N)
N = int(N)

better = 1
if N-(9*t) > 1:
    better = N-(9*t)
for i in range(better, N+1):
    comp = i
    for j in range(t):
        comp += (i // (10**j) % 10)
    if N==comp:
        print(int(i))
        quit()
    if i == N:
        print(0)
        quit()


#자릿수*9작은거부터 생성자를 구해서 출력 없으면 0