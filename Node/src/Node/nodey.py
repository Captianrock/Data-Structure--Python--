'''
Created on Sep 12, 2013

@author: kim
'''
class Node2(object):
    
    def __init__(self,value):
        self._value = value 
        self._nextNode = None
    def getValue(self):
        return self._value
    def setValue(self, value):
        self._value = value 
    def getNextNode(self): 
        return self._nextNode
    def setNextNode(self, node):
            self._nextNode = node 
    def __str__(self):
        return str(self._value)