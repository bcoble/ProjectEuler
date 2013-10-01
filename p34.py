#! usr/bin/env python
""" Project Euler - Problem 34 """

def fact(n):
    if n == 0:
        return 1
    else:
        f = fact(n-1)
        return n * f
        
def algorithm():
    
    cap = 600000 # 9x9!
    total = 0
    for x in range(3, cap):
        sum = 0
        s = str(x)
        for digit in s:
            i = int(digit)
            f = fact(i)
            sum += f
        if sum == x:
            print(x)
            total += sum
    print("Total:",total)    
    
def main():
    algorithm()
    
if __name__ == "__main__":
    main()