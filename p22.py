#! usr/bin/env python
""" Project Euler - Problem 22 """


# Fields
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def calculate(list):
    global alphabet
    total = 0
    count = 1
    for word in list:
        wordTotal = 0                
        wordSum = 0
        for digit in word:
            letter = str(digit).lower()
            value = alphabet.index(letter) + 1
            wordSum += value
        
        wordTotal = wordSum * count
        count += 1
        total += wordTotal
       
    return total
            
def quickSort(list):
    if list == []:
        return []
    else:
        pivot = list[0]
        lesser, equal, greater = partition(list[1:], [], [pivot], [])
        return quickSort(lesser) + equal + quickSort(greater)

def partition(list, l, e, g):
    while list != []:
        head = list.pop(0)
        if head < e[0]:
            l = [head] + l
        elif head > e[0]:
            g = [head] + g
        else:
            e = [head] + e
    return (l, e, g)
        
def algorithm():
    sList = []
    f = open("p22.txt")
    
    allTxt = f.read()
    
    # Parse allTxt into an array
    allList = allTxt.split(",")
    
    for word in allList:
        w = word.strip('"')
        sList.append(w)
        
    sorted = quickSort(sList)
    
    ans = calculate(sorted)
    print("Total:",ans)
    
    f.close()
    
def main():
    algorithm()
    
if __name__ == "__main__":
    main()