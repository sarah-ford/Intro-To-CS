a=float(raw_input("Enter a first number: "))
b=float(raw_input("Enter a second number: "))
c=float(raw_input("Enter a third number: "))
def larger(a,b,c):
    if a>b and a>c:
        return "The largest number is " + str(a)
    if b>a and b>c:
        return "The largest number is " + str(b)
    else:
        return "The largest number is " + str(c)
print larger(a,b,c)

    
