# description: Target Heart Rate Zones- This program calculates Maximum Heart Rate (MHR) and preferred Target Heart Rate (THR) Zones
# author: Sarah Ford
# date: 1/27/17

a=int(raw_input("Please input your age: "))
MHR=220-a
Z11=0.6*MHR
Z12=0.7*MHR
Z21=Z12
Z22=0.8*MHR


print "Your Maximum Heart Rate (MHR) is: ",MHR
print 
print "Please indicate your exercise objective as follows"
print "1 = weight loss, building endurance"
print "2 = weight management, improving cardio fitness"
print "3 = interval workouts"
r=int(raw_input("input your objective: "))
print 

def THeartRate(a):   
    if r<2:
        return "Your Target Heart Rate zone is: "+str(Z11)+" - "+str(Z12)+" beats per minute"
    if 1<r<3:
        return "Your Target Heart Rate zone is: "+str(Z21)+" - "+str(Z22)+" beats per minute"
    if r>2:
        return "Your Target Heart Rate zone is: "+str(Z22)+"+ beats per minute"
print THeartRate(a)
