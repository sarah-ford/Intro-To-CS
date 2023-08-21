#description: This program uses a binary search algorithm to check a given list for a target number and reports the count of target numbers calculated prior to finding a hit
#author: Ford, Sarah
#date: Apr. 2, 2017

def Remove_Dup(Original_List):
    Original_List
    No_Dup_List=[]
    for n in Original_List:
        if n not in No_Dup_List and n<=100 and n>=0:
            No_Dup_List.append(n)
    return No_Dup_List


def sort(No_Dup_List):
    for i in range(1,len(No_Dup_List)):
        value=No_Dup_List[i]
        j=i-1
        while (j>=0) and (No_Dup_List[j]>value):
            No_Dup_List[j+1]=No_Dup_List[j]
            j=j-1
        No_Dup_List[j+1]=value
    return No_Dup_List


def binary_search(No_Dup_List):
    Search_List=No_Dup_List
    rand_num=random.randint(0,100)
    count=0
    small=0
    large=len(Search_List)-1
    median=(small+large)//2
    while Search_List[median]<>rand_num:
        count+=1
        Search_List=No_Dup_List
        rand_num=random.randint(0,100)
        small=0
        large=len(Search_List)-1
        median=(small+large)//2
        print "Target: ",rand_num
        while small<=large:
            median=(small+large)//2
            if Search_List[median]==rand_num:
                break
            elif Search_List[median]<rand_num:
                small=median+1
            else:
                large=median-1            
    return count




Original_List=raw_input("Please enter a list of 10 unique numbers chosen from the inclusive range of 0 to 100: ")
Original_List=Original_List.split(",")
for n in range(len(Original_List)):
    Original_List[n]=int(Original_List[n])


import random

print
No_Dup_List=Remove_Dup(Original_List)
print "Original List: ",No_Dup_List
Sorted_List=sort(No_Dup_List)
print
print "Sorted List: ",Sorted_List
print
Binary_Search=binary_search(No_Dup_List)
print "Count: ",Binary_Search
