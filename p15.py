#! usr/bin/env python
""" Project Euler - Problem 15 """

import math

# Recurser function for the brute force method
def helper(d, r):
    
    if(d == 0 or r == 0):
        return 1

    return helper(d-1, r) + helper(d, r-1)

# This function was used to verify algorithm 1 works correctly
# It was my first solution but has a very high run time, hence
# the development of the better solution (algorithm1)
def algorithm2(n):
    moves = 0
    moves = helper(n, n)
    
    print("Size: ",n, "Moves:", moves)
    
def algorithm1(d):
    n = d*2
    k = n/2
    
    nFactorial = math.factorial(n)
    kFactorial = math.factorial(k)
    
    ans = nFactorial / (kFactorial**2)
    l = int(ans)
    print("Size:",d,"Moves:",l)
    
def main():
    dimension = 20
    algorithm1(dimension)
    #algorithm2(dimension)
    
    
if __name__ == "__main__":
    main()