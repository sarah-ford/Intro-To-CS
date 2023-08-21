
#YES COUNT IS 4 FOR ABC D AND THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG

# COULD DO THIS W/ NESTED LOOPS (THIS COULD BE EXTRA CREDIT PROBLEM)


first=raw_input("enter the first string (no repeating letters): ")
second=raw_input("Enter the second string: ")
first=first.lower()
newfirst=""
for b in range(len(first)):
    if first(b)<>"":
        newfirst=newfirst+first[b]
first=newfirst
print first
second=second.lower()
count=0
for i in range(len(first)):
    for j in range(len(second)):
        if first[i]==second[j]:
            counter+=1
            break
if counter==len(newfirst):
    print "Yes. Count is", counter
else:
    print "No"
print "Version 2"
counter=0
for i in range(len(first)):
    if first[i] in second:
        counter+=1
if counter>=len(first):
    print "Yes. Count is",counter
else:
    print "No"


# KNOW HOW TO PULL THINGS OUT OF STRINGS
# THERE WILL BE AT LEAST TWO PROBLEMS YOU WILL HAVE TO CODE
# MAYBE A 3RD WHERE YOU HAVE TO FIGURE OUT WHAT THE CODE DOES
# THEN EXTRA CREDIT
