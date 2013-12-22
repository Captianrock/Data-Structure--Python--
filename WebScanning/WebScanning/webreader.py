'''
Created on Oct 21, 2013

@author: kim
'''
import nltk
import urllib 
class WebReader:
    def __init__(self, webpage):
        self.tokens = []
        self.webpage = webpage
        opened = urllib.urlopen(self.webpage)
        stuff = opened.read()
        opened.close()
        cleaned = nltk.clean_html(stuff)
        self.tokens = nltk.word_tokenize(cleaned)
        self.tokens = filter(lambda x: x.isalpha(),self.tokens)
        self.tokens = map(lambda x: x.lower(), self.tokens)
    def __iter__(self):
        i = 0 
        while i < len(self.tokens):
            yield self.tokens[i]
            i += 1
            
    