#! /usr/bin/env python
""" Project Euler - Problem 7 """

def isPrime(n):
    prime = True
    
    for i in range(2, n//2):
        if n%i==0:
            prime = False
            break;
            
    if prime==True:
        print("Prime -",n)
    return prime

def algorithm():
    primeCount = 0
    x = 2
    while primeCount<10002:
        if isPrime(x):
            primeCount+=1
        x += 1
        
    ans = x-1
    print("10001th Prime: ", ans)
    
def main():
    algorithm()
  
if __name__ == "__main__":
    main()