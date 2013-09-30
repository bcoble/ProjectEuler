#! usr/bin/env python
""" Project Euler - Problem 12 """

#Imports
from math import *

# Fields
primeList = []
stack = []
copies = [] 
blank = []   

def resetCopies():
    global copies
    global blank
    copies = [0 for i in range(2, 100000)]
      
# Function that determines if a number is prime
def isPrime(n):
    global primeList
    return primeList[n]
 
 # Compiles a list of all the primes numbers under the cap.
 # Most time intensive part of this program, but it allows all 
 # prime look up's under the cap perform in constant time.
def compilePrimes():
    global primeList
    global copies
    global blank
    
    print("Compiling prime list...")
    
    cap = 100000000
    primeList = [True for i in range(2, cap)]
    copies = [0 for i in range(2, 100000)]
    blank = copies
    
    for i in range(2, round(sqrt(cap))):
        if primeList[i] == True:
            for j in range(i**2, cap-2, i):
                primeList[j] = False
                
    print("Compilation complete.")
    
# Function that calculates the prime factorization of a number
def primeFactors(n):
    global stack, copies
    
    # Check first if n is prime
    if isPrime(n):
        stack.append(n)
        copies[n] += 1
        return -1
    
    for i in range(2, round(n//2)):
        #Check primality of the factor first
        if isPrime(i):
            #Then check if it is a factor
            if n%i==0:
                stack.append(i)
                copies[i] += 1
                return n//i
    return -1
    
def calculateDivisors():
    global copies, stack
    product = 1
    
    # Loop through the copies list - this could be bad
    largest = max(stack)
    for i in range(2, largest+2):#len(copies)):
        if copies[i] != 0:
            n = copies[i]
            n += 1
            #print("i: ", i, "n: ",n)
            product *= n
    return product

def algorithm():
    divisors = 0
    nthTriangle = 1
    n = 0
    # Keep making triangle numbers and checking their divisor #.
    while divisors <= 500:
        n += nthTriangle
        divisors = countDivisors(n)
        if(divisors >= 100):
            print(n,"has",divisors,"divisors.")
            print()
        nthTriangle += 1
        
def countDivisors(n):
    global stack, copies
    stack = []
    resetCopies()
    next = primeFactors(n)
    while next != -1:
        next = primeFactors(next)
    
    dNum = calculateDivisors()
    
    return dNum
   
def main():
    compilePrimes()
    algorithm()
    
    
if __name__ == "__main__":
    main()