import sys
N = int(sys.stdin.readline())
case = 0
fac = [1]*(N+1)
for i in range(2, N+1):
    fac[i]= fac[i-1] * i
for i in range(N//2+1):
    case += fac[N-i]//(fac[N-2*i]*fac[i])

print(case%15746)




