'''
Recursion을 통해 반으로 쪼개나가서 한개까지 쪼갠다.decomposition
이후 두개씩 짝을 이뤄서 합쳐나간다. aggregation
'''
import random

def performMergeSort(lstElementToSort):
    #하나까지 쪼개진 recursion 마지막지점 
    #decomposition ->aggregation
    if len(lstElementToSort) == 1:
        return lstElementToSort
    
    #절반으로 쪼개는 과정
    lstSubElementToSort1 = []
    lstSubElementToSort2 = []
    for itr in range(len(lstElementToSort)):
        if len(lstElementToSort)//2 > itr:
            lstSubElementToSort1.append(lstElementToSort[itr])
        else:
            lstSubElementToSort2.append(lstElementToSort[itr])
    
    #쪼개진 리스트 두개를 mergesort하여 리컬젼을 만든다.
    #그렇게 리턴된 각각의 리스트를 다시 넣는다. 이는 이미 리컬젼을 돌면서
    #sorting이 끝난 상태이다.
    lstSubElementToSort1 = performMergeSort(lstSubElementToSort1)
    lstSubElementToSort2 = performMergeSort(lstSubElementToSort2)
    
    #그렇게 리턴된 sorting이 끝난 리스트 두개를 sorting을 생각하면서 합친다.
    idxCount1 = 0
    idxCount2 = 0
    for itr in range(len(lstElementToSort)):
        #둘중하나 다쓰면 나머지로 쭉
        if idxCount1 == len(lstSubElementToSort1):
            lstElementToSort[itr]=lstSubElementToSort2[idxCount2]
            idxCount2 += 1
        #둘중하나 다쓰면 나머지로 쭉
        elif idxCount2 == len(lstSubElementToSort2):
            lstElementToSort[itr]=lstSubElementToSort1[idxCount1]
            idxCount1 += 1
        #비교해서 작은게 앞으로 그리고 커서 한칸뒤로
        elif lstSubElementToSort1[idxCount1] > lstSubElementToSort2[idxCount2]:
            lstElementToSort[itr] = lstSubElementToSort2[idxCount2]
            idxCount2 += 1
        else:
            lstElementToSort[itr] = lstSubElementToSort1[idxCount1]
            idxCount1 += 1
    return lstElementToSort

lstRandom = []
for itr in range(0, 11):
    lstRandom.append(random.randrange(0,100))
print("before : ", lstRandom)
print("After : ", performMergeSort(lstRandom))
