
# Recursion Lab Problems

# Problem 1

# Define a recursive function called power that has two parameters a (a real
# number) and b (b is a nonnegative integer). The function raises a to the
# power of b and returns the result.


a=int(raw_input("Please input a base: "))
b=int(raw_input("Please input a positive power: "))

def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)
    
print power(a,b)
