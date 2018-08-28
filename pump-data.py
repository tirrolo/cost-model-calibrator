#!/usr/bin/python

import sys
import math

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)

if (len(sys.argv)==1):
    print "you need to add at least the seed n (This generator will produce 2^n rows)"
    sys.exit() 

seed = int(sys.argv[1])
numRows = 2**seed

def find_A3(i):
    for x in range(0,seed):
        if (i%(2**(x+1)) == (2**x)-1):
            return seed - x
    return 0

def find_A5(i):
    for k in range(0,seed+1):
        for j in range(0,numRows):
            if(i == (2**(k-1))*(1+2*j)):
                return 2**(seed-k)+j
    return 0

for i in range(0,numRows):
    # A1:
    A1 = 0
    A2 = 0
    if(i>0):
        x = math.log(i,2)
        A1 = int((x + 1)//1)
    # A2    
    A2=i

    # A3
    A3 = find_A3(i)
    
    # A4
    A4 = A3
    
    # A5
    A5 = find_A5(i)
    
    # A6
    A6 = A5

    print("%d, %d, %d, %d, %d, %d" % (A1,A2,A3, A4, A5, A6))
