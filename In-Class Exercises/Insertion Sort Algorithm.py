
 # Insertion Sort Algorithm

 def insertionSort(L):
     for i in range(1, len(L)):
         val=L[i]
         j=i-1
         while (j>=0) and (L[j]>val):
             L[j+1]=L[j]
             j=j-1
        L[j+1]=val
            
