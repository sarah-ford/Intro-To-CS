#description: This program takes a base and a power and prints out a power function
#author: Ford, Sarah
#date: Feb. 15, 2017

def power(b,p):
    result=b
    if p==0:
        print
        return 1
    elif p<0:
        for index in range (p,-1,1):
            result=result*b
        print    
        return 1/result
    else:
        for index in range(p,1,-1):
            result=result*b
        print
        return result


while True:
    try:
        b=float(raw_input("Please enter a base: "))
    except ValueError:
        print
        print "ERROR-- You may only enter integers or decimals!"
        print
        continue
    if isinstance(b,float):
        break
while True:
    try:
        p=int(raw_input("Please enter a power: "))
    except ValueError:
        print
        print "ERROR-- You may only enter integers!"
        print
        continue
    if isinstance(p,int):
        print power(b,p)
        break
  
