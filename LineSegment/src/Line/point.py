'''
Created on Sep 8, 2013

@author: kim
'''
from math import sqrt 
class Point: 
    def __init__(self,x,y):
        self._xCoord= x
        self._yCoord = y 
    def getX(self): 
        return self._xCoord
    def getY(self):
        return self._yCoord
    def distance( self, otherPoint):
        xDiff = self.getX() - otherPoint.getX()
        yDiff = self.getY() - otherPoint.getY() 
        return sqrt(xDiff*xDiff+yDiff*yDiff)
    def __eq__(self,other):
        if(self._xCoord == other._xCoord and self._yCoord == other._yCoord):
            return True
        else:
            return False 