#! usr/bin/env python
""" Project Euler - Problem 36 """

# Imports
from math import *

def isPalindrome(n):
    stringForm = str(n)
    length = len(stringForm)
    count = 1
    for letter in stringForm:
        i = length-count
        if letter != stringForm[i]:
            return False
        count += 1
    if n!=0:
        return True
    else:
        return False

def isBinaryPalindrome(n):
    b = bin(n)
    binaryList = list(str(b))
    newBL = binaryList[2:]
    stringForm = "".join(newBL)
    length = len(stringForm)
    count = 1
    for letter in stringForm:
        i = length-count
        if letter != stringForm[i]:
            return False
        count += 1
    if n!=0:
        return True
    else:
        return False

def algorithm():    
    sum = 0
    for i in range(1000000):
        if isPalindrome(i):
            if isBinaryPalindrome(i):
                print(str(i) + " is a double palindrome.")
                sum += i

    print("Sum: " + str(sum))
    
def main():
    algorithm()
    
if __name__ == "__main__":
    main()