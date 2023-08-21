#description: This program reduces and decodes a coded message
#author: Ford, Sarah
#date: Feb. 25th, 2017


# Strip Function

def strip(string):
    global stripped_string # define a global variable for use in decode function
    stripped_string=""
    for i in range(0,len(string)):
        if ord(string[i])>=97 and ord(string[i])<=122:
            stripped_string=stripped_string+string[i]
        else:
            continue
    return stripped_string

# Decode Function

def decode():
    stripped_string_length=len(stripped_string)
    decoded_string=""
    global offset # define a global variable for use in main section
    offset=0
    while key not in decoded_string:
        count=0
        decoded_string=""
        for i in range(0,stripped_string_length):
            ascii_num=ord(stripped_string[0+count])+offset
            if ascii_num>122:
                decoded_string+=chr(ascii_num-26)
                count+=1
            else:
                decoded_string+=chr(ascii_num)
                count+=1
        offset+=1
    return decoded_string

# Beginning of Program (Main Section)

string=raw_input("Enter the encoded string: ")
string=str.lower(string)
print "Lower case string is: "+string
print


print "With the specials stripped out the string is: "+strip(string)
print

key=raw_input("Enter the code_key: ")
print
decode()
offset=offset-1
print "offset= "+str(offset)
print
print "The decoded string is: "+decode()

