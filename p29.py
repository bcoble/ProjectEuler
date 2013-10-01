#! usr/bin/env python
""" Project Euler - Problem 29 """

# Imports
from math import *

def algorithm():   
    all = []
    for a in range(2, 101): 
        arow = []
        for b in range(2, 101):
            power = a**b
            flag = False
            for x in range(len(all)):
                if all[x] == power:
                    flag = True
            if flag != True:
                all.append(power)
    print(len(all),"distinct terms in the sequence.")
    
def main():
    algorithm()
    
    
if __name__ == "__main__":
    main()