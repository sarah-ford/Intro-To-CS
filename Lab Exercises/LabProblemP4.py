
# Recursion Lab Problems

# Problem 4

# Using recursion, write a function that prints a triangle of stars that is n
# rows high, where n is the function parameter.

def star_triangle(x):
    if x==1:
        print "*"
        return 
    else:
        print (x)*"*"
        star_triangle(x-1)
        return 

