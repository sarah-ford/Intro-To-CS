
# 2)
# Create a list named nums populated with 22,7,16,9,12,10. Print it. Then, using
# a For loop, locate any perfect squares and replace them with their own
# squares. Print the result.

import math

nums=[22,7,16,9,12,10]
print nums

new_list=[]
for n in range(len(nums)):
    sqrt=math.sqrt(nums[n])
    if int(sqrt)==sqrt:
        own_square=(nums[n])**2
        new_list.append(own_square)
    else:
        new_list.append(nums[n])

print new_list


# 3)
# Append the final list in 2) with largest and then the smallest number in that
# list (2 steps). Then, print the length of the new list.

max_num=max(new_list)
min_num=min(new_list)

new_list.append(max_num)
new_list.append(min_num)

print new_list

