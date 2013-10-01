#! usr/bin/env python
""" Project Euler - Problem 27 Classes """

class qHolder:
    " Quadratic's data for coeff's a and b "
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.pList = []
    
    def setA(self, a):
        self.a = a
        
    def setB(self, b):
        self.b = b
        
    def addToPList(self, n):
        self.pList.append(n)
        
    def getA(self):
        return self.a
        
    def getB(self):
        return self.b
        
    def getSize(self):
        return len(self.pList)
        
    def print(self):
        print("A:",self.a,"B:",self.b,"Size:",len(self.pList),"Product:",(self.a*self.b))
        