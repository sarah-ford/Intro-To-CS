
def separate_num(num_string):
    num_string=str(num_string)
    digit_one=num_string[0]
    digit_two=num_string[1]
    digit_three=num_string[2]
    return power_string(digit_one,digit_two,digit_three)

def power_string(digit_one,digit_two,digit_three):
    digit_one=int(digit_one)
    digit_two=int(digit_two)
    digit_three=int(digit_three)
    return (digit_one**3)+(digit_two**3)+(digit_three**3)


num_string=raw_input("Enter a three-digit number: ")
num=int(num_string)
num_string=separate_num(num_string)
while num_string<>num:
    if num_string>num:
        print num,"is not an armstrong number, too big"
        num_string=raw_input("Enter a three-digit number: ")
    elif num_string<num:
        print num,"is not an armstrong number, too small"
        num_string=raw_input("Enter a three-digit number: ")
if num_string==num:
    print num,"is an armstrong number"
