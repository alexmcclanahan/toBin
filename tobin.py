#going to attempt to write a script to convert a decimal integer into binary

import math

#n is your decimal input integer
n = input("Enter a positive decimal integer you wish to obtain the binary representation of: ")
def toBits(n):
    g = n
    xi = int(math.floor(math.log(n, 2)))
    A = [None]*(xi+1)
    for i in range(xi, -1, -1):
        y = n - (2**i)
        if y >= 0:
            A[xi - i] = 1
            n = n - (2**i)
        else:
            A[xi - i] = 0
    for j in range(0, xi+1):
        A[j] = str(A[j])
    final = ''
    for z in range(xi, -1, -1):
        final = A[z] + final
    print "The binary representation of",g, "is:", final

#program call
toBits(n)
