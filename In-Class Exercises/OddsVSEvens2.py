
import random

odd_count=0
even_count=0

random_limit=int(raw_input("Enter n: "))
diff_count=int(raw_input("Enter n: "))

while odd_count-even_count<diff_count:
    test_num=random.randint(1,random_limit)
    if test_num%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1

total_random=odd_count+even_count
print total_random
