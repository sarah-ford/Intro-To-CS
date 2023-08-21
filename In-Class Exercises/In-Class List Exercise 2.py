nums=raw_input("Please enter numbers separated by commas: ")
nums=nums.split(",")
smallest=nums[0]
for n in range(len(nums)):
    if nums[n]<smallest:
        smallest=nums[n]

print smallest
