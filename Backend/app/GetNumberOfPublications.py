import httplib2
from bs4 import BeautifulSoup
import re
from Backend.app.const import *

class GetNumberOfPublications():
    userId = ""
    source = ""

    def addId(self, userId):
        self.userId = userId

    def getSource(self):
        http = httplib2.Http()
        status, response = http.request(BASE_URL+PUB_NUM_URL+str(self.userId)+"&rel=BPP-author")
        soup = BeautifulSoup(response, 'html.parser')
        self.source = soup

    def findNumbers(self):
        text = str(self.source.find_all('h4'))
        x = re.compile('\d+')
        pageNumbers = re.findall(x, text)
        return pageNumbers[1]

    def getNumberOfPublications(self, userId):
        self.addId(userId)
        self.getSource()
        numberOfPublications = self.findNumbers()
        return numberOfPublications
        
          
