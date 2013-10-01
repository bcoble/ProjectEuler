#! usr/bin/env python
""" Project Euler - Problem 23 """

aList = [0 for i in range(28124)]

# Returns a list of the factors of 'n'
def factors(n):
    list = []
    for i in range(1, n):
        if n%i == 0:
            list.append(i)
    return list

# Returns 'True' if n is an abundant number
def isAbundant(n):
    global aList
    
    # First check aList
    if aList[n] == 1:
        return True
    elif aList[n] == -1:
        return False
    # Otherwise compute it
    else:   
        s = 0
        flist = factors(n)
        s = sum(flist)
        if s > n:
            aList[n] = 1
            return True
        else:
            aList[n] = -1
            return False
    
# Returns 'True' if n can be summed by two abundant numbers
def canBeSummed(n):

    for i in range(1, n):
        if isAbundant(i):
            diff = n - i
            if isAbundant(diff):
                return True
       
    return False


def algorithm():
    
    sum = 0
    
    for i in range(1,28124):  
        # Check if 'i' is the sum of two a(n)'s
        if canBeSummed(i) == False:
            print(i,"cannot be summed.")
            sum += i
    
    print("Sum:",sum)
        
    
def main():
    algorithm()
    
    
if __name__ == "__main__":
    main()