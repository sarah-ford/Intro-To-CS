
# HW8 Lab

# 1)
# Create a Python program which will interchange the diagonal on any odd-sided
# square filled with random integers from 1 to 25

import random

size=int(raw_input("Please input an odd square size: "))

square=[[0 for row in range(size)] for col in range(size)]

print
print "Square without random diagonal: "
print
for row in square:
    for col in row:
        print col,
    print
print

row=0
col=0
for num in square:
    square[row][col]=random.randint(1,25)
    row+=1
    col+=1

for row in square:
    for col in row:
        print col,
    print
        
