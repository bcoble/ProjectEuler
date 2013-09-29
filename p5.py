#! /usr/bin/env python
""" Project Euler - Problem 5 """

# Runs the algorithm to find the smallest positive number
# evenly divided by the numbers 1-20
def algorithm():
    product = 1
    for i in range(1,21,2):
        product *= i
    smallest = product * 2
    print(smallest)
        
    n = 2520 # smallest # perfectly divisible by 1-10
    
    while n<product:
        n+= 20
        if checker(n):
            break
    print(n)
    
# Verifies that a number meets the requirements.
def checker(n):
    
    if n%20==0: # 1, 2, 4, 5, 10
        if n%19==0:
            if n%18==0: # 2, 3, 6, 9
                if n%17==0:
                    if n%16==0: # 2, 4, 8
                        if n%14==0: # 2, 7
                            if n%13==0:
                                if n%11==0:
                                    return True
    return False
    
    
def main():
    algorithm()
  
if __name__ == "__main__":
    main()