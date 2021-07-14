import sys
personN = int(sys.stdin.readline())
kg = list(range(personN))
cm = list(range(personN))
dungchiNum = list(range(personN))
for i in range(personN):
    kg[i], cm[i] = map(int, sys.stdin.readline().split())
for j in range(personN):
    count = 1
    for i in range(personN):
        if kg[i] > kg[j] and cm[i] > cm[j]:
            count += 1
    dungchiNum[j] = count

result = ""
for i in range(personN):
    result += str(dungchiNum[i])+" "
print(result.rstrip(" "))