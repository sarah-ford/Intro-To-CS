
# HW6 Lab

# 1)
# Create a list named letters and populate it with the letters a,b,c,d,e,f,g.
# Print the list. Next, replace index positions 2 through 4 with C,D, and E.
# Again, print the altered list. Next remove them and reprint the list. Now,
# clear the list by replacing all of the elements with an empty list. Print the
# result and then print "Done".


letters=['a','b','c','d','e','f','g']
print letters
print
letters[2:5]=['C','D','E']
print letters
print
del letters[2:5]
print letters
print
letters=[0 for pos in letters]
print letters
print
print "Done"
