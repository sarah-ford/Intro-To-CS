import random

question=raw_input("Ask the magic 8 ball: (press Q to quiet) ")
while question <>"Q":
    answers=random.randint(1,4) # number between 1 and 4

    if answers==1:
        print "It is certain"
    elif answers==2:
        print "Outlook is good"
    elif answers==3:
        print "Ask again later"
    elif answers==4:
        print "My sources say no"

    question=raw_input("Ask the magic 8 ball: (press Q to quiet) ")
