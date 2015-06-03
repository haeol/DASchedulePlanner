import requests
import re
from bs4 import BeautifulSoup
from scraper import *
from course import *
import cPickle as pickle

class Professor:
    def __init__(self):
        self.first = "-1"
        self.last = "-1"
        self.subject = "-1"
        self.overall = -1
        self.avg_grade = -1
        self.helpful = -1
        self.clarity = -1
        self.easy = -1

class Crawler:
    def __init__(self):
        pass

    def get_teacher(self, search, subj = 0):
        query = ""
        professors = []
        for token in search.split():
            query += "+" + token
        url = "http://www.ratemyprofessors.com/search.jsp?query=de+anza" + query
        page = requests.get(url).content
        #soup = BeautifulSoup(page)
        for link in soup.findAll('a', href=re.compile('/ShowRatings.jsp?')):
            professors.append(link.get('href'))
        for idx, professor in enumerate(professors):
            professors[idx] = "http://www.ratemyprofessors.com" + professor
        return professors #returns a list of pages of professors based on search

    def get_ratings(self, soup):
        for ratings in soup.findAll("div",{"class":"rating"}):
            print ratings

        #for ratings in soup.find("div",{"class":"rating"}):
        #    print ratings



def get_soup(url):
     return BeautifulSoup(requests.get(url).content)


def get_teacher():
    

def main():
    schedule = pickle.load(open('courses.p', 'r'))
    teachers = set()
    for key in schedule:
        for _class in schedule[key]:
            print _class.professor
            teachers.add(" ".join(_class.professor))
    for t in teachers:
        print t









def fucking_around():
    search = "mary pape"
    query = ""
    tokenized = search.split()
    for token in tokenized:
        query += "+" + token
    url = "http://www.ratemyprofessors.com/search.jsp?query=de+anza" + query

    page = requests.get(url).content
    soup = BeautifulSoup(page)
    professors = []
    for link in soup.findAll('a', href=re.compile('/ShowRatings.jsp?')):
        """
        #print link.get('href')
        for sub in link.find("span",{"class":"sub"}):
            print sub
        """
        professors.append(link.get('href'))

    for idx, professor in enumerate(professors):
        professors[idx] = "www.ratemyprofessors.com" + professor

    print professors




if __name__ == "__main__":
    main()
