#! /usr/bin/env python
""" Project Euler - Problem 4 """

def checkPalindrome(n):
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

def algorithm():

    max = 0
    X = 0
    Y = 0
    
    # Post completion note: improved bounds on the
    # for-loops would prevent repetitive checking
    # (ie for 3x300 and 300x3)
    for x in range(1000):
        for y in range(1000):
            product = x * y
            if checkPalindrome(product):
                print(product, " - ", x, " - ", y)
                if product > max:
                    max = product
                    X = x
                    Y = y
                
    print(max, " x: ", X, " y: ", y)

def main():
    algorithm()
   
if __name__ == "__main__":
    main()