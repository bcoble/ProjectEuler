#! usr/bin/env python
""" Project Euler - Problem 30 """


def algorithm():
    
    total = 0
    
    # Check fifth powers - just picked a really large number
    for x in range(2, 200000):
        s = str(x)
        sum = 0
        for digit in s:
            i = int(digit)
            p = i**5
            sum += p
        if sum == x:
            print(x)
            total += sum
                
    print("Sum:",total)
    
def main():
    algorithm()
    
    
if __name__ == "__main__":
    main()