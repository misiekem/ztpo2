import httplib2
from bs4 import BeautifulSoup
import re
from app.const import *
from time import sleep

class GetUserId():
    name = ""
    surname = ""
    firstLetter = ""
    source = ""

    def addSurname(self, surname, name):
        self.surname = surname
        self.name = name
        self.firstLetter = surname[0]

    def getSource(self):
        http = httplib2.Http()
        status, response = http.request(BASE_URL+AUTHOR_URL+str(self.firstLetter))
        soup = BeautifulSoup(response, 'html.parser')
        self.source = soup

    def findIdBySurname(self):
        href = re.compile('^userHomepage&uId')
        idUrl = ""
        for a in self.source.find_all('a', href=href):
            text = a.find_all(text=True)
            if self.surname in text[0] and self.name in text[0]:
                idUrl = a['href']
                x = re.compile('\d+')
                x = re.findall(x, idUrl)
                return x[0] # value of user id
                break
        

    def getId(self, surname, name):
        self.addSurname(surname, name)
        self.getSource()
        id = self.findIdBySurname()
        return id
        
          
