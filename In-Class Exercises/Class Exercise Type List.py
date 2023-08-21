
L=[2.46,5,'7',8,4.73,'3']

for num in L:
    if type(L[num])==int:
        num=num**2
    elif type(L[num])==float:
        num=round(num,1)
    elif type(L[num])==str:
        num=int(num)

print L
