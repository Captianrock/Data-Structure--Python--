'''
Created on Nov 12, 2013

@author: kim
'''
class Heap: 
    def __init__(self): 
        self.A = [] 
    def insert(self, value) : 
        self.A.append(value)
        position = len(self.A) - 1  
        while self.A[position] > self.A[position/2]: 
            temp = self.A[position]
            self.A[position] = self.A[position/2]
            self.A[position/2] = temp
    def removeTop(self):
        pass

 