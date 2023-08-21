
# Recursion Lab Problems

# Problem 3

# Write a recursive function, named rec find gcd with two parameters a and b, to
# implement Euclid's algorithm. Here is a reminder on how the algorithm works:

# Euclid's algorithm is an algorithm used to calculate the greatest common
# denominator (GCD) of two numbers a and b, where a<b<0. To start the algorithm,
# we calculate "a mod b." If the resulting value c is equal to 0, then b is the
# GCD of a and b. If not, we then repeat the process starting with "b mod c."
# Eventually, the result of this calculation will be 0, meaning that c is the
# greatest common denominator.


def rec_find_gcd(a,b):
    c=a%b
    if c==0:
        return b
    else:
        return rec_find_gcd(b,c)
