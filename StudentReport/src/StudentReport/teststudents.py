'''
Created on Sep 21, 2013

@author: kim
'''
from filereader import StudentFileReader
from filereader import StudentRecord

FILE_NAME = "students.txt"

def main():
    reader = StudentFileReader(FILE_NAME)
    reader.open()
    record = reader.fetchRecord()    
    print record.idNum
    print record.firstName
    print record.lastName
    print record.classCode
    print record.gpa
    record = reader.fetchRecord()
    print record.idNum
    print record.firstName
    print record.lastName
    print record.classCode
    print record.gpa
    record = reader.fetchRecord()
    print record.idNum
    print record.firstName
    print record.lastName
    print record.classCode
    print record.gpa
main()
    