#! usr/bin/env python
""" Project Euler - Problem 21 """

# Fields
master = [-1 for i in range(1000000)]

# Calculates the function 'd(n)'
def functionD(n):
    global master
    
    if n == 0:
        return
    
    list = []
    for i in range(1,n):
        if n%i == 0:
            list.append(i)
    
    sum = 0
    for number in list:
        sum += number
    
    master[n] = sum

    
# Checks if the numbers are friends
def isAmi(n):
    global master

    d = master[n]
    if d != -1:
        d2 = master[d]
        if d2 != -1 and d2 != d:
            if d2 == n:
                print(d, "and", d2, "are friends.")
                return True
    else:
        return False
    
def algorithm():
    aList = []
    
    for i in range(10000):
        functionD(i)
    
    for i in range(2, 10000):
        if isAmi(i):
            aList.append(i)
    
    sum = 0
    for number in aList:
        sum += number
    print(aList, "sums to",sum)
    
    
def main():
    algorithm()
    
if __name__ == "__main__":
    main()