
# Recursion Lab Problems

# Problem 2

# Define a function bin rep that takes an integer as its argument and returns
# its binary representation in a list.


def bin_rep(x):
    if x<2:
        return [x]
    else:
        return bin_rep(x/2)+[x%2]
