#description: This program allows the user to input a list of scores and then computes the mean, median, and standard deviation
#author: Ford, Sarah
#date: March. 26, 2017


# Functions

def mean(nums):
    total_sum=0
    for n in range(widget_num):
        nums[n]=int(nums[n])
        total_sum+=nums[n]
    return float(total_sum)/float(widget_num)

def sortem(nums):
    for i in range(widget_num):
        for j in range(widget_num-1):
            if nums[j]>nums[j+1]:
                t=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=t
    return nums

def median(nums):
    if widget_num%2==0:
        for n in range(widget_num):
            nums[n]=int(nums[n])
        median=(float(nums[widget_num/2-1])+float(nums[(widget_num/2)]))/2
        return median
    else:
        for n in range(widget_num):
            nums[n]=int(nums[n])
        median=float(nums[(widget_num/2)])
        return median

def std_dev(nums):
    diff_sqrd_sum=0
    for n in range(widget_num):
        nums[n]=int(nums[n])
        diff_sqrd_sum+=((nums[n]-mean)**2)
        import math
    s=math.sqrt(diff_sqrd_sum/(widget_num-1))
    return s
            
# Main Section

import random
widget_num=random.randint(20,30)
print "Input",widget_num,"widget scores"
nums=raw_input("Input widget scores separated by commas: ")
nums=nums.split(",")
for n in range(widget_num):
    nums[n]=int(nums[n])
print nums

mean=mean(nums)

sortem=sortem(nums)

median=median(nums)

std_dev=std_dev(nums)

print
print "The list of numbers sorted is: ",sortem
print
print "The mean for",len(nums)," values is",round(mean,2)
print
print "The median for",len(nums),"values is",median
print
print "The standard deviation for",len(nums),"values is",round(std_dev,2)

