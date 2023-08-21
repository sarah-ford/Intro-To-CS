
A=[[10,6],[18,8],[8,9]]
B=[[5,4],[10,4],[5,7]]
M=[[0,0],[0,0],[0,0]]

def MatSub(A,B):
    print A
    print B
    for row in range(len(A)):
        print
        for col in range(len(A[0])):
            M[row][col]=A[row][col]+B[row][col]
            print M[row][col],
    return ""


print MatSub(A,B)

