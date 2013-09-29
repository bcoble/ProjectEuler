#! /usr/bin/env python
""" Project Euler - Problem 1 """

def computeSum():
    x = 0
    sum = 0
    
    while x < 1000:
	    if x%3==0 or x%5==0:
	        sum += x
	    x += 1
    print("The sum is: ", sum)
    
def main():
    print("Welcome to Problem 1.")
    computeSum()

if __name__ == "__main__":
	main()