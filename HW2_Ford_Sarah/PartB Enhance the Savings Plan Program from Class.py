# description: Enhance the Savings Plan Program from Class
# author: Sarah Ford
# 1/27/17

#Developing Programs Example
#Get Information from user

print

name=raw_input("What is your name? ")
print "Hello ",name
print 
print "I understand you want to save money to buy something."
print 
item=raw_input("What are you interested in buying? ")
print 
balance=float(raw_input("OK, what is the cost of the item? $"))
print 
#catch potential input errors

if(balance<0):
    print ("Looks like you might have saved enough already")
    balance=0
    payment=1
else:
    payment=float(raw_input("Enter how much you wish to save each period: $"))
    if(payment<=0):
        payment=float(raw_input("Your payment must be positive. Please enter a positive value $"))
    if(payment<=0):
        print "Since you again entered a positive value, your assumed payment will be 1 per period."
        payment=1

#Calculate the necessary number of payments

num_remaining_payments=balance/payment
remaining=balance%payment
print
print "You must make",int(num_remaining_payments), "payments of $", float(payment)
if remaining<>0:
    print "And one payment of $", float(remaining)
