#! /usr/bin/env python
""" Project Euler - Problem 9 """

def algorithm():
    
    for i in range(500):
        for j in range(i,1000):
            cap = 1000-i
            for k in range(j, cap):
                sum = i + j + k
                if sum == 1000:
                    if checkTri(i,j,k):
                        print(i, ", ", j, ", ", k)
                        print(sum)
                        if sum == 1000:
                            print("Found it!")
                            print(i*j*k)
                            break

def checkTri(a, b, c):
    if a<b<c:
        a2 = a**2
        b2 = b**2
        c2 = c**2
        if a2 + b2 == c2:
            return True
        else:
            return False
    else:
        return False
        
def main():
    algorithm()
  
if __name__ == "__main__":
    main()