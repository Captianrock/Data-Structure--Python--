'''
Created on Sep 21, 2013

@author: kim
'''
class StudentFileReader :
  def __init__( self, inputSrc ):
    self._inputSrc = inputSrc
    self._inputFile = None
    self._abc = -1
    self._values = list()
  def open( self ):
    self._inputFile = open(self._inputSrc, "r" )
  def close( self ):
    self._inputFile.close()
    self._inputFile = None

  def fetchRecord( self ): 
    lines = self._inputFile.readline()
    if self._abc < 12: 
        self._abc += 1 
        if lines == "":
            return None
        temp = lines.replace(":", " ").split()
        record = StudentRecord()
        record.idNum = int(temp[0])
        record.firstName = temp[1].rstrip()
        record.lastName = temp[2].rstrip()
        record.classCode = int(temp[3])
        record.gpa = float(temp[4])
        self._values.append(record)
    return  self._values[self._abc]

class StudentRecord :
  def __init__( self ):
    self.idNum = 0
    self.firstName = ""
    self.lastName = ""
    self.classCode = 0
    self.gpa = 0.0
