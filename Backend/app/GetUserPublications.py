from bs4 import BeautifulSoup
from selenium import webdriver
import re
from app.const import *
from unidecode import unidecode

class GetUserPublications():
    basicUrl3 = "&rsAt="
    source = ""
    userId = ""
    numbersOfPublications = 0
    page = 0
    wd = None

    def addId(self, userId):
        self.userId = userId

    def addNumbersOfPublications(self, numbersOfPublications):
        self.numbersOfPublications = int(numbersOfPublications)

    def addPageNumbers(self, pageNumbers):
        self.pageNumbers = pageNumbers

    def startSession(self):
        self.wd = webdriver.PhantomJS('app/libs/phantomjs.exe')
        self.wd.get(BASE_URL+PUB_NUM_URL+str(self.userId)+"&rel=BPP-author")

    def getSource(self, page):
        self.wd.get(BASE_URL+PUBLICATIONS_URL+str(self.userId)+"&rsAt="+str(self.page))
        self.source = BeautifulSoup(self.wd.page_source, 'html.parser')

    def getPublications(self):
        rows = []
        mniswPoints = []
        title = []
        typeName = []
        publicationForm = []
        publicationDate = []
        # finds table rows containing information about publications
        for a in self.source.find_all('td', style="border-bottom:#ddd 1px solid;"):
            rows.append(a.contents)
        # iterate rows and appends correct data to specific list 
        for a in range(len(rows)):
            if a==0:
                pass
            else:
                row = rows[a]
                src = row[0]
                text = src.find_all(text=True)
                for i, j in enumerate(text):
                    if j==' typ: ':
                        typeName.append(unidecode(text[i+1]))
                        title.append(unidecode(text[i-1]))
                        continue
                    elif j==' Punktacja czasopisma na Liście MNiSW: ':
                        mniswPoints.append(unidecode(text[i+1]))
                        continue
                    elif j==' Data wydania: ':
                        publicationDate.append(unidecode(text[i+1]))
                        continue
                    elif j==' Forma publikacji: ':
                        publicationForm.append(unidecode(text[i+1]))
                        continue
                titleMaxIndex = len(title)
                # filling empty places in rows with None
                while titleMaxIndex > len(publicationForm):
                    publicationForm.append("None")
                while titleMaxIndex > len(publicationDate):
                    publicationDate.append("None")
                while titleMaxIndex > len(mniswPoints):
                    mniswPoints.append("None")
        return title, typeName, publicationForm, publicationDate, mniswPoints
                


    def getAllPublications(self, userId, numbersOfPublications):
        self.addId(userId)
        self.addNumbersOfPublications(numbersOfPublications)
        # if number of publications is not greater than 20 check only one url
        if self.numbersOfPublications <= 20:
            self.page = 0
            self.startSession()
            self.getSource(self.page)
            title, typeName, publicationForm, publicationDate, mniswPoints = self.getPublications()
            self.wd.close()
            return title, typeName, publicationForm, publicationDate, mniswPoints
        # number of publications is more than 20  
        elif self.numbersOfPublications > 21:
            self.page = 0
            self.startSession()
            self.getSource(self.page)
            # get first 20 records
            title, typeName, publicationForm, publicationDate, mniswPoints = self.getPublications()
            pages = self.numbersOfPublications/20
            pages = int(pages)
            # go to next url's containing max 20 records each
            while pages>=1:
                self.page += 20
                self.getSource(self.page)
                title1, typeName1, publicationForm1, publicationDate1, mniswPoints1 = self.getPublications()
                title += title1
                typeName += typeName1
                publicationForm += publicationForm1
                publicationDate += publicationDate1
                mniswPoints += mniswPoints1
                pages-=1
            self.wd.close()
            return title, typeName, publicationForm, publicationDate, mniswPoints




    
        
          
