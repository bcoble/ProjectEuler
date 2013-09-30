#! /usr/bin/env python
""" Project Euler - Problem 11 """

# Imports
from random import *

SUPERLIST = []

# Fields
hMax = 0
vMax = 0
dMax = 0

hxStart = 0
hyStart = 0
vxStart = 0
vyStart = 0
dxStart = 0
dyStart = 0


def buildList():
    list = []
    for i in range(10):
        horz = []
        for j in range(10):
            num = randint(0,10)
            horz.append(num)
        list.append(horz)
    
    #print(list)
    return list

def checkHorz(l):
    global hMax
    global hxStart
    global hyStart
    
    # Loop over the list
    for s in range(len(l)):
        line = l[s]
    
        # Iterate over the list
        size = len(line)
        for i in range(size-3):
            xStart = i
            value = calculateHorz(line, xStart)
            if(value > hMax):
                hMax = value
                hxStart = xStart
                hyStart = s 
                #print(hMax)
                #print("^^^")
        
def calculateHorz(l, x):
    product = 1
    for i in range(x, x+4):
        product *= l[i]
    return product


def checkVert(l):
    global vMax
    global vxStart
    global vyStart
    
    # Loop over the list and get columns
    for i in range(len(l)):
        column = i
        for j in range(len(l)-3): # Guna cheat this check, 
                                        # since I'm working with a
                                        # square
            yStart = j
            value = calculateVert(l, column, yStart)
            if value > vMax:
                vMax = value
                vxStart = column
                vyStart =  yStart
                #print(vMax)
                #print("'''")
            
    
def calculateVert(l, c, y):
    product = 1
    for i in range(y, y+4, 1):
        #print("x: ",c, " y: ",i)
        row = l[i]
        product *= row[c]
    #print(product)
    #print("^^^")
    return product
    
    
def checkDiag(list):
    global dMax, dxStart, dyStart
    size = len(list)
    
    # Top left -> bottom right
    for i in range(size-3): # Moving the top-left y down
        for j in range(size-3): # Moving the top-left x right
            value = calculateRightDiag(list, j, i)
            if value > dMax:
                dMax = value
                dxStart = j
                dyStart = i
                #print(dMax)
                #print("***")
        
    # Top right -> bottom left
    for i in range(size-3): # Moving the top-right y down
        for j in range(3, size): # Moving the top-right x right
            
            value = calculateLeftDiag(list, j, i)
            if value > dMax:
                dMax = value
                dxStart = j
                dyStart = i
                #print(dMax)
                #print("---")
    
def calculateRightDiag(list, x, y):
    product = 1
    for i in range(x, x+4):
        
        row = list[y]
        product *= row[i]
        #print(row, " x: ",i," y:",y, "value: ",row[i])
        y += 1
    #print("product: ",product)
    #print("===")
    return product
    
def calculateLeftDiag(list, x, y):
    product = 1
    for i in range(x, x-4, -1):
        #print("x: ",i," y:",y)
        row = list[y]
        product *= row[i]
        y += 1
    #print(product)
    return product
    
def compareMax():
    global vMax, hMax, dMax
    max = vMax
    
    print("*----------*")
    print("Horz: ", hMax)
    print("Vert: ", vMax)
    print("Diag: ", dMax)
    
    if hMax > vMax:
        max = hMax
    
    if dMax > max:
        max = dMax
        
    print("Max: ", max)

def initialize():
    global SUPERLIST
    SUPERLIST = []
    SUPERLIST.append([8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8])
    SUPERLIST.append([49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0])
    SUPERLIST.append([81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65])
    SUPERLIST.append([52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91])
    SUPERLIST.append([22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80])
    SUPERLIST.append([24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50])
    SUPERLIST.append([32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70])
    SUPERLIST.append([67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21])
    SUPERLIST.append([24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72])
    SUPERLIST.append([21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95])
    SUPERLIST.append([78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92])
    SUPERLIST.append([16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57])
    SUPERLIST.append([86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58])
    SUPERLIST.append([19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40])
    SUPERLIST.append([4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66])
    SUPERLIST.append([88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69])
    SUPERLIST.append([4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36])
    SUPERLIST.append([20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16])
    SUPERLIST.append([20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54])
    SUPERLIST.append([1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48])
    #print(SUPERLIST)
    
    global tiny
    tiny = []
    tiny.append([1, 1, 5, 5, 5, 5])
    tiny.append([1, 1, 1, 5, 5, 1])
    tiny.append([1, 1, 5, 1, 6, 1])
    tiny.append([1, 5, 1, 1, 5, 6])
    tiny.append([1, 1, 1, 1, 1, 1])
    tiny.append([1, 1, 1, 1, 1, 1])
    #print(tiny)
    
    
def algorithm():
    # Set up list
    initialize()
    
    # Compile list (temp one currently)
    #list = buildList()
    
    # Check horzizontal
    checkHorz(SUPERLIST)
    #checkHorz(tiny)
    
    # Check vertical
    checkVert(SUPERLIST)
    #checkVert(tiny)
    
    # Check diagonals
    checkDiag(SUPERLIST)
    #checkDiag(tiny)
    
    # Compare maxes and return greatest product
    compareMax()
    
def main():
    algorithm()
    
if __name__ == "__main__":
    main()