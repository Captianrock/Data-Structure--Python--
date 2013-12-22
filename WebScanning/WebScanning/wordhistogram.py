'''
Created on Oct 21, 2013

@author: kim
'''
from webreader import WebReader
class WordHistogram: 
    def __init__(self, token):
        self.dicto = {}
        self.token = token
        for word in self.token:
            if word in self.dicto:
                self.dicto[word] += 1
            else:
                self.dicto[word] = 1
      
    def __iter__(self):
        for key in self.dicto.items():
                key1 = key[0]
                value = key[1]
                yield key1+ " " + str(value)
                
                
            
                 
            
            
                  
            
            