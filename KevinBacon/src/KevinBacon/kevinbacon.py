'''
Created on Oct 30, 2013

@author: kim
'''
 #f2e4d16a67dd9d2154b9b2a6e311d8ab - keys to the kingdom
import requests  

class BaconFinder: 
    def __init__(self,apikey):
        self.apikey = apikey
        self.allrealnames = {}
        self.allnames = {}

    def find(self,actor):
        self.commonnames = []
        self.safelist = []
        self.allrealnames = {}
        self.allnames = {} 
        allchosen = [] 
        self.safeactor2 = None
        self.safelist = []  
        actor=actor.split()
        firstname = actor[0]
        lastname = actor[1]
        if firstname =="Kevin" and lastname =="Bacon":
            self.commonnames.append("Kevin Bacon")
            return str(self.commonnames)+" Kevin Bacon number of 0"
        thechosenone = requests.get("http://api.themoviedb.org/3/search/person?api_key="+self.apikey+"&query=" + firstname + "+" + lastname)
        chosendict =  thechosenone.json()
        theactorresult = chosendict['results']
        self.theidnum = str(theactorresult[0]['id'])
        self.allrealnames[self.theidnum] = str(theactorresult[0]['name'])
        self.commonnames.append(str(theactorresult[0]['name']))
        thechosenmovies = self.getMovies(self.theidnum)
        for x in thechosenmovies: 
            allchosen.extend(self.getActors(x))
        allchosen = list(set(allchosen)) 
        for x in allchosen:
            self.allnames[x] = x
        oldlist = allchosen
        oldlist2 = list(allchosen) 
        self.safelist.append(oldlist)
        verdict = self.goBacon(oldlist)
        if verdict is True:
            self.commonnames.append("Kevin Bacon")
            return str(self.commonnames) + " Kevin Bacon number of " + str(len(self.commonnames) - 1)
        z = 0
        while verdict is False:
            thesecondmovies = []
            thesecondactor = []
            for x in oldlist2:
                thesecondmovies.extend(self.getMovies(x))
            for x in thesecondmovies:
                thesecondactor.extend(self.getActors(x)) 
            for x in thesecondactor:
                self.allnames[x] = x
            oldlist2 = list(thesecondactor)
            verdict = self.goBacon(thesecondactor)
        if verdict is True:
            self.commonnames.append("Kevin Bacon")
            self.commonnames.insert(1,self.safelist[0])
            return str(self.commonnames) + " Kevin Bacon number of " + str(len(self.commonnames) - 1)
        return "This is too much please stop. There is too much Kevin Bacon"    
    def goBacon(self,listy):
        verdict = self.EqualBacon()
        safeactor = None
        safelist= []
        while len(listy) > 0: 
            if verdict is True:
                if safeactor != None:
                    self.commonnames.insert(1,self.allrealnames[safeactor])
                return True
                break
            else:
                thenewid = listy.pop(0)
                safeactor = thenewid
                safelist.append(self.allrealnames[safeactor])
                temp = []
                thenewmovies = self.getMovies(thenewid)
                for x in thenewmovies:
                    temp.append(self.getActors(x))    
                for x in temp:
                    for l in x: 
                        self.allnames[l] = l              
                verdict = self.EqualBacon()
        self.allnames = {}
        self.safelist = list(safelist)
        return False
     
    def EqualBacon(self):
        try:
            self.allnames[4724]
            return True 
        except:
            KeyError
            return False
               
    def getMovies(self,actorid): 
        temp = []
        actorid = str(actorid) 
        actor = requests.get("http://api.themoviedb.org/3/person/"+actorid+"/credits?api_key="+self.apikey)
        actordic = actor.json()
        actordic2 = actordic['cast']
        i = 0 
        while i < len(actordic2):
            idnum = actordic2[i]['id']
            temp.append(idnum)
            i += 1
        return temp  
    
    def getActors(self,movieid):
        d=[]
        movieid = str(movieid)
        movie = requests.get("http://api.themoviedb.org/3/movie/"+movieid+"/credits?api_key="+self.apikey) 
        moviedic = movie.json()
        moviedic2 = moviedic['cast']
        i = 0 
        while i < len(moviedic2):
            idnum = moviedic2[i]['id']
            try:
                self.allrealnames[idnum] = str(moviedic2[i]['name'])
            except UnicodeEncodeError:
                self.allrealnames[idnum] = moviedic2[i]['name']
            self.allnames[idnum] = moviedic2[i]['id']
            d.append(idnum) 
            i += 1 
        return d 