
# Selection Sort Algorithm

def selectionSort(L):

    for j in range(0,len(L)-1):

        # Step 1 - find the location of the smallest
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
