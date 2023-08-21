# description: Low Cost Mortgage Loans for Couples Program; This program screens for couples seeking low cost mortgage loans. Couples need 5 points to qualify.
# author: Sarah Ford
# date: 2/2/17


point=0
print "For the applicants:"
Age1=int(raw_input("Person One, Enter your age: "))
Age2=int(raw_input("Person Two, Enter your age: "))
if (25<=Age1<=30 and 23<=Age2<=35) or (25<=Age2<=30 and 23<=Age1<=35):
    point=point+1
    print "For the loan officer:"
    Med=float(raw_input("Enter median print of homes in this area during the past 12 months: $"))
    print
    print "For the applicants:"
    Ann=int(raw_input("Enter years in relationship: "))
    if 1<=Ann<=5:
        point=point+1
        Emp=str(raw_input("Both gainfully employed for 48 weeks, Y or N? "))
        if Emp=="Y":
            point=point+1
            Price=int(raw_input("Enter price of home: $"))
            if Med-Price>=5000:
                point=point+1
                print "Enter credit scores. They must be between 300 and 850."
                C1=int(raw_input("Enter person one's credit score: "))
                C2=int(raw_input("Enter person two's credit score: "))
                if 700<=C1<=850 and 700<=C2<=850:
                    point=point+1
                    if point==5:
                        print "Congratulations. You have qualified: 5 points"
                        print
                        def rate(C1,C2):
                            print "For the loan officer"
                            r=float(raw_input("Please enter the present interest rate: "))
                            if (C1+C2)/2<750:
                                return "Your interest rate is: " + str(r) + "%"
                            if 750<=(C1+C2)/2<=774:
                                return "Your interest rate is: " + str(r-1.0/8.0) + "%"
                            if 775<=(C1+C2)/2<=799:
                                return "Your interest rate is: " + str(r-1.0/4.0) + "%"
                            if (C1+C2)>=800:
                                return "Your interest rate is: " + str(r-3.0/8.0) + "%"
                        print rate(C1,C2)
                    else:
                        print "Sorry.",point,"points. You do not qualify."
                else:
                    print "Sorry.", point,"points. You do not qualify."
            else:
                print "Sorry.", point,"points. You do not qualify."
        else:
            print "Sorry.", point,"points. You do not qualify."
    else:
        print "Sorry.", point,"point. You do not qualify."
else:
    print "Sorry.", point,"points. You do not qualify."

               
        
    



    

