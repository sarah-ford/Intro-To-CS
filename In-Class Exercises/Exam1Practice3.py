#LEARN HOW TO FIND PRIME NUMBERS AND HAVE CODE PREPARED

# The function isPrime(n) receives an integer n and returns true if n is a prime number, False otherwise

n=int(raw_input("Please enter an integer n: "))

def isPrime(n):
    sqrt_n=n^(1/2)
    for i in range(2,sqrt_n):
        if sqrt_n%i==0:
            return False
        else:
            return True
print isPrime(n)
