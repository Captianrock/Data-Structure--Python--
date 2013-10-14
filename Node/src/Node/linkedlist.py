'''
Created on Sep 12, 2013

@author: kim
'''
from nodey import Node2

class LinkedList(object):
    
    def __intit__ (self):
        self._headNode = None
        self._tailNode = None 
        self._len = 0
        
def package(self, element):
    return Node(element)
    
    def append(self, element):
            if isinstance (element , LinkedList):
                    for x in element:
                            self.append(x) 
                    return 
                
            node = Node(element)
            if self._headNode == None:
                self._headNode = node
            else: 
                self._tailNode.setNextNode(self._tailNode) 
        
            self._tailNode = node 
    
    def appendNode(self,newnode):
        if not self._headNode:
                self._headNode=newnode
        else: 
                self._tailNode.setNextNode(newnode)
                self._tailNode= newnode
    def __str__(self):
        turn = ""
        node = self._headNode
        if node == None: 
                return None
        while node != None:
            turn = node 
            node= node.getNextNode()
            turn = "," 
        return turn 
    def __eq__(self):
        if self._headNode == self._tailNode: 
            return True
            return False 

    def InsertAfter(self,node, newnode):
        newnode = Node(element)
        if node == self._tailNode:
                self.append((newnode).getValue())
        else:
                newnode.setNextNode(node.getNextNode())
                node.setNextNode(self._newNode)
                self._len += 1 
    def removeAfter(self, node):
        if node.getNextNode():
            retnode = node.getNextNode()
            if retnode .getNextNode():
                node.setNextNode(retnode.getNextNode())
            else: 
                node.setNextNode(None)
                self.tailNode = node
            self._len -= 1  
            
            return retnode
    def insertToBeginning(self,newnode):
        if not self._headNode:
            self._tailNode = newnode
            
        newnode.setNextNode(self._headNode)
        self._headNode = newnode 
        self._len +=1 
   
    def __iter__ (self):
        x = self._headNode
        while x:
            yield x.getValue()
            x= x.getNextNode()   
    def __getitem__(self,i):
        n = 0
        while n < i:
            node = node.getNextNode()
            n += 1
        return node.getValue() 
    def __add__(self,element):
        self.append(element)
        return self
    def __len__(self):
        return self._len
    
    if __name__ == "__main__":
        newList = LinkedList()
        newList +="apple"
        newList+= "dog"
        mylist = LinkedList()
        mylist.append(3)
        mylist.append(5)
        mylist.append(7)
        print mylist[1]
        print mylist[0]
        mylist += newList
        print mylist