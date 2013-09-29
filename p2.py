#! /usr/bin/env python
""" Project Euler - Problem 2 """

# Fields
memory = [-1 for x in range(100)]
memory.insert(0, 0)
memory.insert(1, 1)

# Function that computes the nth fibonacci number.
def fib(n):

    if memory[n]==-1:
        print("Nothing stored for fib ", n)
        ans = fib(n-1) + fib(n-2)
        memory.insert(n, ans)
    else:
        print("Looking up from memory")
        ans = memory[n]
    
    return ans

# Function that runs the algorithm.
def computeProblem():
    valueCap = 4000000
    cap = 100
    x = 3
    sum = 0
    
    while x < cap:
        if x%3==0:
            temp = fib(x)
            if temp< valueCap:
                sum += temp
        x += 1
    
    print("Answer: ", sum)
    
def main():
    computeProblem()
    
if __name__ == "__main__":
    main()