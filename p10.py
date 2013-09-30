#! /usr/bin/env python
""" Project Euler - Problem 10 """

from math import *

def algorithm():
    sum = 0
    cap = 2000000
    isPrimeList = [True for i in range(2, cap)]
    
    for i in range(2, round(sqrt(cap))):
        if isPrimeList[i] == True:
            for j in range(i**2, cap-2, i):
                isPrimeList[j] = False
    
    # The previous loops set all the non-primes to false.
    # Simply add all the spots that are still true.
    for i in range(2, cap-2):
        if isPrimeList[i] == True:
            sum += i
            
    print("Sum:", sum)
    
def main():
    algorithm()
  
if __name__ == "__main__":
    main()