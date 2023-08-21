# NOW MAKE PROBLEM WHERE ENTER INTEGER AND PULL OUT GREATEST PAIR

num=int(raw_input("Enter an integer: "))
snum=str(num)
numlen=len(snum)


if numlen%2!= 0:
    numlen=len(snum)-1
if numlen!= 0:
    largest=int(snum[0]+snum[1])
    for n in range(2,numlen,2):
        x=int(snum[n]+snum[n+1])
        if x>largest:
            largest=x
    print largest
else:
    print "String too short"
