#DO ALL OF THE LETTERS IN THE FIRST STRING APPEAR IN THE SECOND?

a=raw_input("Enter the first string (no repeating letters): ")
b=raw_input("Enter the second string: ")
alen=len(a)
blen=len(b)
count=0
for i in range(0,alen):
    for x in range(0,blen):
        if a[0:] in b:
            count+=1
        else:
            count=0
print count
