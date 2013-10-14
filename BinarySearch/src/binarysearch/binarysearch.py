'''
Created on Sep 26, 2013

@author: kim
'''
class Binary: 
    def __intit__ (self, key, theList):
        self._theList = theList
        self._key = key 
    def search(self,key,theList):
        low = 0 
        high = len(theList) - 1 
        midpoint = (high + low) / 2 
        while (low <= high): 
            if(theList[midpoint] > key):
                high = midpoint -1 
                midpoint = (high - midpoint)/2   
            if(theList[midpoint] < key):
                low = midpoint + 1 
                midpoint = (low + midpoint) / 2 
            else:
                return midpoint 
        return None 
    