# How many random positive integers between 1 and m have to be chosen before
# the odds outnumber the evens by n?
# THIS COULD BE A TEST PROBLEM


n=int(raw_input("Enter n: "))
m=int(raw_input("Enter m: "))

import random
count=0
counte=0
counto=0
while True:
    number=random.randint(1,n)
    count=0
    if number%2==0:
        counte=count+1
    if isinstance(number%2,int):
        counto=count+1
    if counte-counto==n:
        print count
        break
        

#initialize some variables then get into the (while) loop
