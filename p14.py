#! usr/bin/env python
""" Project Euler - Problem 14 """

# Fields
stack = []
max = 0
number = 0

def collatz(n):
    global stack
    stack.append(n)
    
    if n == 1:
        return -1
    if n%2 == 0:
        next = n//2     
    else:
        next = 3*n + 1
        
    collatz(next)

def algorithm():
    global stack, max, number
    # Will need to improve this loop. 
    # Ok for now
    for i in range(999999, 2, -1):
        collatz(i)
        size = len(stack)
        if size > max:
            max = size
            number = i
            print(number,"has a chain length of", size)
            
        if i%100000 == 0: # visual cue
            print("***",i,"***")
        stack = []
    
    
def main():
    algorithm()
    
    
if __name__ == "__main__":
    main()