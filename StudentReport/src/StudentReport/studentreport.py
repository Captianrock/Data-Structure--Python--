
from filereader import StudentFileReader
# Name of the file to open.
FILE_NAME = 'students.txt'
 
class StudentReport:
    def __init__(self):
        self._theList = list()
        
    def loadRecords(self, filename):
        reader = StudentFileReader(filename)
        reader.open()
        record = reader.fetchRecord()
        while record is not None :
            self._theList.append( record )
            record = reader.fetchRecord()
        reader.close()
        return self._theList
    def sortByName(self):
        self._theList.sort(key = lambda x: (x.lastName, x.firstName))
        
    def sortByid(self):
        self._theList.sort(key = lambda y: y.idNum)
    def getAvgGPA(self):
        gpal = []
        y = 0
        for x in self._theList:
            gpal.append(x.gpa)
            y += 1 
        gpal2 = map(lambda i: i/y, gpal) 
        return round(reduce(lambda w,z: w+z , gpal2),2)
    def __str__(self):
    # The class names associated with the class codes.
        body = "" 
        classNames = [ "", "Freshman", "Sophomore", "Junior", "Senior" ]
        header = "LIST OF STUDENTS\n".center(50)+"\n" +( "%-5s  %-25s  %-10s  %-4s" % ('ID', 'NAME', 'CLASS', 'GPA'))+( "\n%5s  %25s  %10s  %4s\n" % ('-' * 5, '-' * 25, '-' * 10, '-' * 4))
        for record in self._theList:
            body += ( "%5d  %-25s  %-10s  %4.2f\n" % \
                  (record.idNum, \
                   record.lastName + ', ' + record.firstName,
                   classNames[record.classCode], record.gpa ))

        last1 = ( "-" * 50 )  
        last2 = "Average GPA: " + str(self.getAvgGPA())  
      
        return header + body + "\n" +last1 + "\n" + last2 
if __name__ == "__main__":
        s= StudentReport()
        s.loadRecords(FILE_NAME)
        s.sortByName()
        s.getAvgGPA()
        print str(s)
        
