import math
def hypotenuse(base,height):
    return math.sqrt((base**2)+(height**2))
base=float(raw_input("Enter the base of the triangle: "))
height=float(raw_input("Enter the height of the triangle: "))
hyp = hypotenuse(base, height)
print "The result is: ", hyp


              
