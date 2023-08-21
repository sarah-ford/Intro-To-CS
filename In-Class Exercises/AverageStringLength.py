# Enter a string of words separated by commas (No blanks).
# Average the length of the words

word_string=str(raw_input("Please enter a string of words: "))
str_len=len(word_string)


tot_word_len=0
num_words=0
word=""

for i in range (0,str_len):
    if word_string(i) !=",":
        word=word+word_string(i)
        print word
    if word_string(i)=="," or i==str_len-1:
        num_words=num_words+1
        tot_word_len=tot_word_len+len(word)
        word=""

avg_word_len=float(tot_word_len)

    
