
# Write a function called secondSmallest that receives a list of integers (not
# in sorted order), and returns the second smallest element in the list. If the
# list contains 1 element, then just return that element. If the list contains
# 0 elements, then return None.
# **NOTE**
# For this problem don't use the sort function on the list. You should iterate
# through the list to find the second smallest element.



def secondSmallest():
   for n in range(1,len(smallist)):
        small=smallist[0]
        if len(smallist)==1:
            return smallist[0]
        elif smallist==[]:
            return None
        elif smallist[n]<small:
            small=smallist[n]
   smallist.remove(small)
   for i in range(1,len(smallist)):
      secondsmall=smallist[0]
      if len(smallist)==1:
         return smallist[0]
      else:
         if smallist[i]<secondsmall:
            secondsmall=smallist[i]
   return secondsmall


smallist=raw_input("Please enter a list of integers: ")
smallist=smallist.split(",")
print "The second smallest number is: ",secondSmallest()
