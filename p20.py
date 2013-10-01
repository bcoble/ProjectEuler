#! usr/bin/env python
""" Project Euler - Problem 20 """

import math

def algorithm():

    f = math.factorial(100)
    sum = 0
    for digit in str(f):
        sum += int(digit)
    
    print("Sum of 100!:",sum)
    
def main():
    algorithm()
    
if __name__ == "__main__":
    main()