#description: This program opens and reads a file, converts the file information into a two-dimensional list format, and extracts information about ratings by restaurant and cuisine
#author: Ford, Sarah
#date: May. 3, 2017

f = open('restaurants.HW9.txt','r')
lines = f.readlines()
nested = [[s.lstrip().rstrip() for s in line.rstrip().split(',')] for line in lines]
print nested

# Prints Out List Of Data From File

print
print

print "2-D List Format"
print

for i in range(len(nested)):
    print nested[i][0],",",nested[i][1],",",nested[i][2],",",nested[i][3],",",nested[i][4]


# Prints Out 2-D List Format of File


L_cuisine=[]
for i in range(len(nested)):
    if nested[i][2] not in L_cuisine:
        L_cuisine.append(nested[i][2])
        
# Compiles List of Cuisines Without Repeats

L_cuis=[]
L_cuis_rate=[]
for i in L_cuisine:
    if L_cuis_rate<>L_cuis:
        L_cuis_rate.append(L_cuis)
    L_cuis=[]
    for n in range(len(nested)):
        if i==nested[n][2]:
            L_cuis.append(nested[n][4])
L_cuis_rate.append(L_cuis)
            
# Compiles List of Lists Where Each Sub-List Contains All Ratings for One Cuisine

L_avg=[]
for i in range(len(L_cuis_rate)):
    added=0
    for n in range(len(L_cuis_rate[i])):
        L_cuis_rate[i][n]=float(L_cuis_rate[i][n])
        added+=L_cuis_rate[i][n]
    avg=added/len(L_cuis_rate[i])
    avg=round(avg,2)
    L_avg.append(avg)

# Compiles List Where Each Element is the Average for One Cuisine

highest_avg=max(L_avg)
highest_avg_index=L_avg.index(max(L_avg))
lowest_avg=min(L_avg)
lowest_avg_index=L_avg.index(min(L_avg))
print
print "a) The cuisine with the highest average rating and the rating: ",L_cuisine[highest_avg_index],", rated",highest_avg
print
print "b) The cuisine with the lowest average rating and the rating: ",L_cuisine[lowest_avg_index],", rated",lowest_avg

# Prints Out Cuisines With Highest and Lowest Ratings


L_rate = []
L_restaurant=[]
for n in range(len(nested)):
    nested[n][4]=float(nested[n][4])
    L_rate.append(nested[n][4])
    L_restaurant.append(nested[n][0])

# Compiles List of Ratings and List of Restaurants
             
highest_rating=max(L_rate)
highest_rating_index=L_rate.index(max(L_rate))
lowest_rating=min(L_rate)
lowest_rating_index=L_rate.index(min(L_rate))
print
print "c) The restaurant with the highest rating and the rating: ",L_restaurant[highest_rating_index],", rated",highest_rating

# Prints Out Restaurant With Highest Rating

L_dollar=[]
for i in range(len(nested)):
    L_dollar.append(nested[i][3])

# Compiles List Where Each Element is a Dollar Rating for One Restaurant

L_dollar_len=[]
for i in range(len(L_dollar)):
    dollar_len=len(L_dollar[i])
    L_dollar_len.append(dollar_len)
    
# Compiles List Where Each Element is Length of Dollar Rating for One Restaurant

high_dollar_len=max(L_dollar_len)

exp_index=[]
for i in range(len(L_dollar_len)):
    if L_dollar_len[i]==high_dollar_len:
        exp_index.append(i)
print
print "d) The most expensive restaurant(s) with the dollar rating: "
for n in exp_index:
    print L_restaurant[n],",",high_dollar_len*"$"

# Prints Out Most Expensive Restaurant(s) and Rating(s)


print
print "e) The restaurant in Boston with the lowest rating and the rating: ",L_restaurant[lowest_rating_index],", rated",lowest_rating

# Prints Out Restaurants With Lowest Rating

