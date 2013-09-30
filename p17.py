#! usr/bin/env python
""" Project Euler - Problem 17 """

# Fields
sub20 = [3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8] # 1, 2, 3... 19
doubles = [6,6,5,5,5,7,6,6] # 20, 30, 40... 90
HUND = 7
AND = 3

# Returns the number of letters if n was written out in words
def countLetters(n):
    count = 0
    word = str(n)
    
    # 1-9
    if (len(word)== 1):
        count += sub20[n-1]
    
    # 10-99
    if (len(word) == 2):
        # 10-19
        tens = int(word[0])
        if(tens == 1):
            count += sub20[n-1]
        # 20-99
        elif(tens > 1):
            ones = int(word[1])
            count += doubles[tens-2]
            if(ones != 0):
                count += sub20[ones-1]

    # 100-999   
    if (len(word) == 3):
        hunds = int(word[0])
        tens = int(word[1])
        ones = int(word[2])
        
        # Count the hundred's place
        count += sub20[hunds-1]
        count += HUND
        
        # Count the ten's place
        if(tens > 1):
            count += doubles[tens-2]
        elif(tens == 1):
            teens = word[1:]
            t = int(teens)
            count += sub20[t-1]
        
        # Count the one's place
        if(ones != 0 and tens != 1):
            count += sub20[ones-1]
            
        # Count and's
        count += AND
        if(tens == 0 and ones == 0):
            count -= AND
            
        print("N:",word,"H:",hunds,"T:",tens,"o:",ones,"=",count)
    
    return count
   
def algorithm():

    countLetters(115)
    countLetters(342)

    letterCount = 0
    for i in range(1,1000):
        letterCount += countLetters(i)
       
    letterCount += 11 # one thousand
    print("Answer:",letterCount)
    
def main():
    algorithm()
    
    
if __name__ == "__main__":
    main()