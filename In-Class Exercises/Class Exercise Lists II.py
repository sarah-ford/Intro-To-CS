
L=[23,18,45,7,17,2,3]

def selectionSort(L):
    for j in range(0,len(L)-1):

        #Step 1 - find the location of the smallest
        # element in L[j:] and exchange it with L[j]
        minVal=L[j]
        minIndex=j
        for k in range(j+1,len(L)):
            if L[k]<minVal:
                minVal=L[k]
                minIndex=k

        # Swap min with element at index j
        L[minIndex]=L[j]
        L[j]=minVal

    return L

print selectionSort(L)

import random

rand=random.randint(0,20)


for i in range(5):
    print ([random.randint(0,20) for x in range(4)] for y in range(5))
