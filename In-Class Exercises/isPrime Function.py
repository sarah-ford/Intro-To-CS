x=int(raw_input("Enter an integer: "))

def isPrime(x):
    if x==2:
        return True
    if x==1:
        return False
    for i in range (2,x):
        if x%i==0:
            return False
    return True


if isPrime(x):
    print x,"is prime"
else:
    print x,"is not prime"


count=0
num=1
while count<=5:
    if isPrime(num):
        print num
        count+=1
    num+=1
