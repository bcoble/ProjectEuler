#! usr/bin/env python
""" Project Euler - Problem 13 """

def algorithm():
    f= open("p13.txt")
    sum = 0
    for line in f:
        value = int(line)
        sum += value
    
    print()
    print("Sum: ",sum)
    f.close
    
def main():
    algorithm()
     
if __name__ == "__main__":
    main()