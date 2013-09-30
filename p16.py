#! usr/bin/env python
""" Project Euler - Problem 16 """

def algorithm():
    
    # Compute 2**1000
    n = 2**1000
    
    s = str(n)
        
    sum = 0
    for l in s:
        sum += int(l)

    print("Sum:",sum)
    
def main():
    algorithm()
    
    
if __name__ == "__main__":
    main()