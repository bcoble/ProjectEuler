#! usr/bin/env python
""" Project Euler - Problem 25 """

# Fields
memory = [-1 for x in range(100000)]
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

def algorithm():
    
    size = 0
    i = 0
    while size != 1000:
        num = fib(i)
        i += 1
        size = len(str(num))
    
    print(i,"is the first term in the Fibonacci sequence to contain 1000 digits.")
    
def main():
    algorithm()
    
    
    
if __name__ == "__main__":
    main()