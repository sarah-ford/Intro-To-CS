
# CS1 2017S Class Exercise Diagonal Sum


import random

n=int(input("Input n(the side)of an n x n odd-sided square: "))

SQ=[[random.randint(1,5) for x in range(n)] for y in range(n)]

print SQ

print
for i in range(n):
    print
    for j in range(n):
        print "%4i"%SQ[i][j],

down=0
for i in range(n):
    down=down+SQ[i][i]

up=0
for i in range(n-1,-1,-1):
    up=up+SQ[i][n-1-i]

print

if down>up:
    print "\n Down diagonal sum is greater: ",down
elif up>down:
    print "\n Up diagonal sum is greater: ",up
else:
    print "\n The diagonal sums are equal: ",down
