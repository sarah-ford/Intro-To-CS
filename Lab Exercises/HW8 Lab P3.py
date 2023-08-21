
# 3)
# Write a Python program to create an n(rows) x m(columns) list filled with
# random integers from 1 to 100, then find any cell where the sum of the row,
# column indices of that cell in the list is odd, then take the contents of that
# cell and double it.


import random

n=int(raw_input("Please enter a row number: "))
m=int(raw_input("Please enter a column number: "))


rand_list=[[random.randint(1,100) for x in range(n)] for y in range(m)]

for x in rand_list:
    for y in x:
        print y,
    print

for x in rand_list:
    for y in x:
        
        if index_sum%2<>0:
            rand_list[x][y]=rand_list[x][y]*2

for x in rand_list:
    for y in x:
        print y,
    print
