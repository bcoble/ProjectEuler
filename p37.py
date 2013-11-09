#! usr/bin/env python
""" Project Euler - Problem 37 """

# Imports
from math import *
from prime import *

# Fields
pList = []

def listToInt(l):
    s = ""
    for i in range(len(l)):
        s += l[i]
    return int(s)

def isTruncatableLeft(n):
    if isPrime(n) == False:
        return False
        
    text = str(n)
    string = list(text)
    size = len(string)
    
    if size == 1:
        if isPrime(n):
            return True
    
    if size!= 0:
        left = listToInt(string[1:])
        return isTruncatableLeft(left)       
    
def isTruncatableRight(n):
    if isPrime(n) == False:
        return False
        
    text = str(n)
    string = list(text)
    size = len(string)
    
    if size == 1:
        if isPrime(n):
            return True
    
    if size!= 0:
        right = listToInt(string[:size-1])
        return isTruncatableRight(right)
    
def algorithm():    
    compilePrimes(10010000)
    count = 0
    sum = 0
    # Loop through primes
    for i in range(9, 10000000,2):
        if count == 11:
            break
        if(isPrime(i)):
            res = isTruncatableLeft(i) and isTruncatableRight(i)
            if(res == True):
                print("***** " + str(i) + " ******")
                count += 1
                sum += i
    print("Total truncatable primes:" + str(count))
    print("Sum: " + str(sum))
    
def main():
    algorithm()
    
if __name__ == "__main__":
    main()