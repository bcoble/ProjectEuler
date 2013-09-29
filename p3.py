#! /usr/bin/env python
""" Project Euler - Problem 3 """

# Fields
TEST_NUMBER = 600851475143
factors = []

def algorithm(n):
    
    previous = primeFactors(n)
    next = 0
    
    while next!=1:
        next = primeFactors(previous)
        if next == previous:
            break
        previous = next

    print("factors", factors)
    # Visual check. A better implementation would store if
    # each was a prime and then compare a list of all the 
    # factors for the greatest prime factor
    for pair in factors:
        print(" *** ")
        isPrime(pair[0])
        isPrime(pair[1])

# Takes an integer n and returns the highest 
def primeFactors(n):
    factor1=2
    factor2 = 0
    while factor1<n:
        if n%factor1==0:
            factor2 = n//factor1
            pair = factor1, factor2
            factors.append(pair)
            break
        factor1 += 1
    
    return factor2

# Function that determines if a number is prime or not.
def isPrime(n):
    prime = True
    
    for i in range(2, n//2):
        if n%i==0:
            prime = False
            print("Not Prime -",n)
            break;
    if prime==True:
        print("Prime -",n)
    return prime
    
def main():
    algorithm(TEST_NUMBER)
    
if __name__ == "__main__":
    main()