#! usr/bin/env python
""" Project Euler - Prime Functions """

# Imports
from math import *

# Fields
primeList = []

# Function that determines if a number is prime
def isPrime(n):
    global primeList
    return primeList[n]
    
# Compiles up to the nth prime    
def compilePrimes(n):
    global primeList
    
    cap = n
    primeList = [True for i in range(2, cap)]
    
    for i in range(2, int(round(sqrt(cap)))):
        if primeList[i] == True:
            for j in range(i**2, cap-2, i):
                primeList[j] = False
    primeList[0] = False
    primeList[1] = False
    
    