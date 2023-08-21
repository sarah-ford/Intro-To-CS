a=int(raw_input("Enter a first integer: "))
b=int(raw_input("Enter a second integer: "))
def larger(a,b):
    if a>b:
        return "The first number is greater"
    if a<b:
        return "The second number is greater"
    else:
        return "The two numbers are equal"
print larger(a,b)
