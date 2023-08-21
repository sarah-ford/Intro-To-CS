#description: This program does a Grommit industry sales forecast
#author: Ford, Sarah
#date Feb. 15, 2017

while True:
    try:
        UG=float(raw_input("Please enter initial sales for UG: "))
    except ValueError:
        print
        print "ERROR-- You may only enter integers or decimals!"
        print
        continue
    if isinstance(UG,float):
        break
while True:
    try:
        GI=float(raw_input("Please enter initial sales for GI: "))
    except ValueError:
        print
        print "ERROR-- You may only enter integers or decimals!"
        print
        continue
    if isinstance(GI,float):
        break
while True:
    try:
        rate_UG=float(raw_input("Please enter annual % increase for UG: "))
    except ValueError:
        print
        print "ERROR-- You may only enter integers or decimals!"
        print
        continue
    if isinstance(rate_UG,float):
        break
while True:
    try:
        rate_GI=float(raw_input("Please enter annual % increase for GI: "))
    except ValueError:
        print
        print "ERROR-- You may only enter integers or decimals!"
        print
        continue
    if isinstance(rate_GI,float):
        break

print
print "GROMMIT INDUSTRY FORECAST"
print
print "Year",'\t','UG','\t','GI'

def sales():
    for x in range(2026):
        if UG>(1.25*GI):
            return "In the final year UG's sales exceeded GI's sales by more than 25%"
            break
        elif GI>(1.25*UG):
            return "In the final year GI's sales exceeded UG's sales by more than 25%"
            break
        else:
            return ""
            break
if UG>GI:
    year=range(2017,2027)
    cross_year=0
    for x in year:
        print x,'\t',UG,'\t',GI
        UG=round((UG+(UG*(rate_UG)/100)),1)
        GI=round((GI+(GI*(rate_GI)/100)),1)
        if UG>GI:
            cross_year=x+1
        if GI>UG:
            cross_year=x+1
            break
    for x in range(cross_year,2027):
        print x,'\t',UG,'\t',GI
        UG=round((UG+(UG*(rate_UG)/100)),1)
        GI=round((GI+(GI*(rate_GI)/100)),1)
               
    print           
    print sales()
    print
    if GI>UG:
        print "The sales crossed in ",cross_year
    if UG>GI:
        print "The sales never crossed"
        

elif UG<GI:
    year=range(2017,2027)
    cross_year=0
    for x in year:
        print x,'\t',UG,'\t',GI
        UG=round((UG+(UG*(rate_UG)/100)),1)
        GI=round((GI+(GI*(rate_GI)/100)),1)
        if UG<GI:
            cross_year=x+1
        if UG>GI:
            cross_year=x+1
            break
    for x in range(cross_year,2027):
        print x,'\t',UG,'\t',GI
        UG=round((UG+(UG*(rate_UG)/100)),1)
        GI=round((GI+(GI*(rate_GI)/100)),1)

    print
    print sales()
    print
    if UG>GI:
        print "The sales crossed in ",cross_year
    if UG<GI:
        print "The sales never crossed"

else:
    year=range(2017,2027)
    cross_year=0
    for x in year:
        print x,'\t',UG,'\t',GI
        UG=round((UG+(UG*(rate_UG)/100)),1)
        GI=round((GI+(GI*(rate_GI)/100)),1)
        if UG==GI:
            cross_year=x+1
        if UG>GI or UG<GI:
            cross_year=x+1
            break
    for x in range(cross_year,2027):
        print x,'\t',UG,'\t',GI
        UG=round((UG+(UG*(rate_UG)/100)),1)
        GI=round((GI+(GI*(rate_GI)/100)),1)
        
    print
    print sales()
    print
    if UG>GI or UG<GI:
        print "The sales crossed in ",cross_year
    if UG==GI:
        print "The sales never crossed"
    



        

    
