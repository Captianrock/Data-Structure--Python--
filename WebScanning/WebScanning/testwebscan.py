'''
Created on Oct 21, 2013

@author: kim
'''
from webreader import WebReader
from wordhistogram import WordHistogram
page = WebReader("http://www.cs.wm.edu/~rfd/")
h = WordHistogram(page)
for x in h: 
    print x
    