#! usr/bin/env python
""" Project Euler - Problem 27 """

# Imports
from c27 import *
from math import *

# Fields
primeList = []
max = qHolder(1, 1)

# Function that determines if a number is prime
def isPrime(n):
    global primeList
    return primeList[n]
    
# Compiles up to the nth prime    
def compilePrimes(n):
    global primeList
    
    cap = n
    primeList = [True for i in range(2, cap)]
    
    for i in range(2, round(sqrt(cap))):
        if primeList[i] == True:
            for j in range(i**2, cap-2, i):
                primeList[j] = False
    primeList[0] = False
    primeList[1] = False

# The quadratic formula for this problem.
def formula(a, b, n):
    return n**2 + (a*n) + b

# Function that contains the solution's algorithm
def algorithm():
    global max

    compilePrimes(100000) 
    # Loop through 'a' and 'b' values
    for i in range(1, 1000): # i = a
        i2 = -1 * i
        for j in range(1, 1000): # j = b
            j2 = -1 * j
            
            # Now set up the qHolders
            q1 = qHolder(i, j)
            q2 = qHolder(i2, j)
            q3 = qHolder(i2, j2)
            q4 = qHolder(i, j2)
            qList = [q1, q2, q3, q4]
            
            # Loop through qHolders
            for q in qList:
                # Test n-values until the value is not prime
                value = 2
                n = 0
                while(isPrime(value)):
                    value = formula(q.getA(), q.getB(), n)
                    q.addToPList(value)
                    n += 1
                if max.getSize() < q.getSize():
                    max = q
                    max.print()
                               
    
def main():
    algorithm()
    
    
if __name__ == "__main__":
    main()