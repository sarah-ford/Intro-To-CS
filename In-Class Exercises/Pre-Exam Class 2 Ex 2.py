import random
print "I am thinking of a number between 1 and 100"


Guess_Flag=False
Target=random.randint(1,100)

Guess_Flag=int(raw_input("Enter a guess: "))

while Guess_Flag==False:
    if Guess_Flag>Target:
        print "Too high"
    elif Guess_Flag<Target:
        print "Too low"
    else:
        print "Correct"
        Guess_Flag=True


