
# Recursion Lab Problems

# Problem 7

# Super Digit


def super_digit(n):
    n=str(n)
    if len(n)==1:
        return n
    else:
        return int(n[0])+int(super_digit(n[1:]))
