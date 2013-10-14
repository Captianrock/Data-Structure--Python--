'''
Created on Sep 8, 2013
lin
@author: kim
'''
from point import Point  

class LineSegment: 
    def __init__( self, startPoint, endPoint):
        self._pointA = startPoint 
        self._pointB = endPoint 
    def endPointA(self):
            return self._pointA
    def endPointB(self):
            return self._pointB 
    def length (self):
        return self._pointA.distance(self._pointB)
    def isVertical (self): 
        return self._pointA.getX() == self._pointB.getX()
    def isHorizontal(self):
        return self._pointA.getY() == self._pointB.getY()
    def isParallel(self,otherLine):
        return self.slope() == otherLine.slope()
    def isPerpendicular(self,otherLine):
        return self.slope() == 1/otherLine.slope()
    def slope(self):
        if self.isVertical():
            return None
        elif self.isHorizontal():
            return 0
        else: 
            run = self._pointB.getX() - self._pointA.getX()
            rise = self._pointB.getY() - self._pointA.getY()
        return rise / run 
    def midpoint(self):
        Xpoint = (float)(self._pointA.getX() + self._pointB.getX())/2
        Ypoint = (float)(self._pointA.getY() + self._pointB.getY())/2
        mid = Point(Xpoint, Ypoint)
        return mid 
    def __str__ (self):
        Xa = self._pointA.getX() 
        Ya = self._pointB.getX()
        Xb = self._pointA.getY() 
        Yb = self._pointB.getY() 
        return "(" + str(Xa)+ ", "+ str(Xb) + ")#(" + str(Ya) + ", " + str(Yb) + ")"
    
        
    
    
    
    
    
    
    
    