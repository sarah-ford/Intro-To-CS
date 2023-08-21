
# Test Problem


import random

col_num=int(raw_input("Enter a new column size between 2 and 9: "))
row_num=int(raw_input("Enter a new row size between 2 and 9: "))


L=[[random.randint(0,10) for x in range(col_num)] for y in range(row_num)]

print L


largest_col_sum=0
for col in range(col_num):
    col_sum=0
    for row in range(row_num):
        col_sum=col_sum+L[row][col]
    if col_sum>largest_col_sum:
        largest_col_sum=col_sum
print

for row in range(0,row_num):
    print ""
    for col in range(0,col_num):
        print "%4i"%L[row][col]
    print ("\n")

    print "Largest Column Sum is: ",largest_col_sum



