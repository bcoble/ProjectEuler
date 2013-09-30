#! /usr/bin/env python
""" Project Euler - Problem 6 """

def algorithm():
    sum = 0
    sum2 = 0
    for i in range(101):
        sum += i**2
        sum2 += i
    
    print(sum)
    print(sum2)
    ans = sum2**2-sum
    print(ans)
    
def main():
    algorithm()
  
if __name__ == "__main__":
    main()