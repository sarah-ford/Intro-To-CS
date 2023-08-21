#description: This program creates an odd-sided Magic Square, where the sum of each row, column, and diagonal adds up to the same number
#author: Ford, Sarah
#date: Apr. 9, 2017



# The Magic Square Function Creates the Magic Square, placing consecutive numbers
# in their correct places such that the sums of all rows, columns, and diagonals
# are equivalent.

def Magic_Square():


    row=0
    col=(size/2)
    num=1

    SQ[row][col]=num

    for pos in range(0,size-1):
        for indices in range(0,size+1):
            if SQ[row][col]==0:
                num+=1
                SQ[row][col]=num
            else:
                row-=1
                col+=1
                num+=1
                if row>=0 and col<size and SQ[row][col]==0:
                    SQ[row][col]=num
                elif row>=0 and col<size and SQ[row][col]<>0:
                    row+=2
                    col-=1
                    SQ[row][col]=num
                elif row<0 and col<size:
                    row+=size
                    SQ[row][col]=num
                elif col>=size and row>=0:
                    col-=size
                    SQ[row][col]=num
                else:
                    row+=2
                    col-=1
                    SQ[row][col]=num            


    print
    for x in SQ:
        for y in x:
            print y,
        print
    return ""

# The Row Sum Check Function checks if the sums of all rows are equal. If they
# are, the function returns the sum. If not, the function returns False.

def Row_Sum_Check(Magic_Square):

    sum_row=0
    row=0
    col=0
    for index in range(size):
        sum_row+=SQ[row][col]
        row+=1


    row=0
    col=0
    for col in range(size):
        row=0
        next_sum_row=0
        for row in range(size):
            next_sum_row+=SQ[row][col]
            row+=1
        if next_sum_row<>sum_row:
            return False
    return next_sum_row

# The Col Sum Check Function checks if the sums of all columns are equal. If
# they are, the function returns the sum. If not, the function returns False.

def Col_Sum_Check(Magic_Square):
    sum_col=0
    row=0
    col=0
    for index in range(size):
        sum_col+=SQ[row][col]
        col+=1

    row=0
    col=0
    for col in range(size):
        col=0
        next_sum_col=0
        for row in range(size):
            next_sum_col+=SQ[row][col]
            col+=1
        if next_sum_col<>sum_col:
            return False
    return next_sum_col

# The Diag Sum Check Function checks if the sums of both diagonals are equal. If
# they are, the function returns the sum. If not, the function returns False.

def Diag_Sum_Check(Magic_Square):
    sum_diag1=0
    row=0
    col=0
    for pos in range(size):
        sum_diag1+=SQ[row][col]
        row+=1
        col+=1


    sum_diag2=0
    row=size-1
    col=size-1
    for pos in range(size):
        sum_diag2+=SQ[row][col]
        row-=1
        col-=1
    if sum_diag1==sum_diag2:
        return sum_diag1
    else:
        return False


# Main Program Section

print "This program creates an odd-sided Magic Square,"
print " where the sum of each row, column and diagonal"
print " adds up to the same number"
print
size=int(raw_input("Input the size of an nxn odd-sided square: "))
SQ =[[0 for x in range(size)] for y in range(size)]
print
print Magic_Square()
print

if Row_Sum_Check(Magic_Square)==Col_Sum_Check(Magic_Square) and Col_Sum_Check(Magic_Square)==Diag_Sum_Check(Magic_Square):
    print "The sum of each row, column, and diagonal is: ",Row_Sum_Check(Magic_Square)

