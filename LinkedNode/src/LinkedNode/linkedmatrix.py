'''
Created on Sep 30, 2013

@author: kim
'''
from node import Node

class LinkedMatrix (object): 
    def __init__(self,x,y,defaultValue):
        self.x = x 
        self.y = y
        self._defaultValue = defaultValue
        self._HeadNode = Node(defaultValue)
        self.NodeArray = []
        temp = self._HeadNode
        z = 0
        u = self.y
        A = []
        B = [] 
        for number in range(0, self.y - 1):
            aftertemp = Node(defaultValue)
            temp.south = aftertemp
            aftertemp.north = temp
            temp = aftertemp
        temp = self._HeadNode
        start = temp.south
        while z < self.y:
            for number in range(0, self.x - 1):
                aftertemp = Node(defaultValue)
                temp.east = aftertemp
                aftertemp.west = temp
                temp = aftertemp
            z += 1 
            temp = self._HeadNode
            for w in range (0,z):
                temp = temp.south
        temp = self._HeadNode
        for number in range(0, self.x):
            A.append(temp)
            temp = temp.east            
        while u >= 2:
            temp = start 
            for number in range(0,self.x):
                if(temp.east != None):
                    B.append(temp)
                    temp = temp.east
                else:
                    B.append(temp)
            for number in range(0,self.x):
                A[number].south = B[number]
                B[number].north = A[number]
            A = B
            B = []
            u = u -1 
            start = start.south
        A = [] 
        B = []  

            
    def __str__(self):
        hi = ""
        temp1 = self._HeadNode
        reset = temp1
        for lol in range(self.y):
            for hey in range(self.x):
                if(temp1 != None):
                    hi += str(temp1.getValue())+ " "
                    temp1 = temp1.east
                else:
                    hi += " " 
            reset = reset.south
            temp1 = reset
            hi += "\n" 
        return hi


    def __getitem__(self,index):
        temp = self._HeadNode
        col = index[0]
        row = index[1]
        for lol in range(0, row):
            temp = temp.south
        for haa in range(0, col):
            temp = temp.east
        return temp.getValue()
    
    def __setitem__(self,index,a):
        col = index[0] 
        row = index[1]
        temp = self._HeadNode
        for lol in range(0, row):
            temp = temp.south
        for haa in range(0, col):
            temp = temp.east
        temp.value = a 
        
    def __iter__(self):
        temp = self._HeadNode
        counter = temp 
        z = self.x*self.y
        while(z > 0): 
            if(temp != None):
                yield temp.getValue()
                temp = temp.east
                z = z - 1 
            else:
                temp = counter.south
                counter = temp.south
                 
        
    def insertRowAfter(self,rowIndex):
        a=[]
        b = []
        c=[]
        temp = self._HeadNode
        if(rowIndex != 0):
            for index in range(0, rowIndex):
                temp = temp.south
        tempcount = temp
        belowtemp = temp.south
        for index in range (0,self.x):
            a.append(tempcount)
            tempcount = temp.east
        if(belowtemp is None):
            newNode = Node(self._defaultValue)
            temp.south = newNode
            newNode.north = temp
            temp = newNode
            for lol in range(1,self.x):
                newNode =Node(self._defaultValue)
                temp.east = newNode
                newNode.west = temp
                b.append(temp)
                temp = newNode
            for number in range(0,self.x - 1):
                a[number].south = b[number]
                b[number].north = a[number]
            self.y = self.y + 1 
        else: 
            belowtemp1 = belowtemp
            for index in range (1,self.x): 
                b.append(belowtemp1)
                belowtemp1 = belowtemp1.east
            newNode = Node(self._defaultValue)
            temp.south = newNode
            belowtemp.north = newNode
            newNode.south = belowtemp
            newNode.north = temp 
            temp = newNode
            for lol in range(1,self.x):
                newNode =Node(self._defaultValue)
                temp.east = newNode
                newNode.west = temp
                c.append(temp)
                temp = newNode
            for number in range (0,self.x-1):
                a[number].south = c[number]
                b[number].north = c[number]
                c[number].north = a[number]
                c[number].south = b[number]
        self.y += 1 
    def insertColumnAfter(self, colIndex):
        temp = self._HeadNode
        if(colIndex != 0):
            for index in range(0, colIndex):
                temp = temp.east
        nextcol = temp.east
        if(nextcol is None):
            for yolo in range(self.y):
                newNode = Node(self._defaultValue)
                temp.east = newNode
                newNode.west = temp
                temp = temp.south 
            temp = self._HeadNode
            reset = temp
            for haha in range(1,self.y):
                for yolo in range(self.x):
                    if(yolo != self.x - 1):
                        temp = temp.east 
                    else:
                        aftertemp = temp.south
                        temp.south = aftertemp 
                        aftertemp.north = temp
                reset = reset.south
                temp = reset
            self.x += 1 
        else:
            A = []
            u = self.y
            for yolo in range(self.y):
                newNode = Node(self._defaultValue)
                temp.east = newNode
                nextcol.west = newNode
                newNode.east = nextcol
                newNode.west = temp 
                temp = temp.south 
                nextcol = nextcol.south 
            self.x += 1 
            temp = self._HeadNode
            reset = temp
            z = 0
            z1 = 0
            while z1 < self.y:
                while z < colIndex+1:
                    temp = temp.east 
                    z +=1
                A.append(temp)
                reset = reset.south
                temp = reset
                z1 += 1 
            i = 0 
            while i < len(A)-1:
                A[i].south = A[i+1]
                A[i+1].north = A[i]
                i += 1 
                
            
    def removeRowAfter(self, rowIndex):
        temp = self._HeadNode
        for index in range(0,rowIndex+1):
            temp = temp.south
        abovetemp = temp.north
        belowtemp = temp.south
        if(abovetemp is None and belowtemp is not None):
            for number in range(0, self.x-1):
                belowtemp.north = None
                belowtemp = belowtemp.east
        elif(abovetemp is not None and belowtemp is None):
            for number in range(0,self.x-1):
                abovetemp.south = None
                abovetemp = abovetemp.east
        else:
            belowtemp.north = abovetemp
            abovetemp.south = belowtemp
        self.y = self.y - 1 
            
    def removeColumnAfter(self, colIndex):
        A = []
        B= []
        temp = self._HeadNode
        for jo in range(colIndex+1):
            temp = temp.east
        left = temp.west
        right = temp.east 
        if(right is None):
            print "hey"
            for number in range(self.y-1):
                temp.east = None
                temp = temp.south
            self.x = self.x - 1
        else:
            for yolo in range(self.y):
                A.append(left)
                left = left.south
                B.append(right)
                right = right.south
            i = 0 
            while i < len(A):
                A[i].east = B[i]
                B[i].west = A[i]
                i += 1 
            self.x = self.x -1      