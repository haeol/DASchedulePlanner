from scraper import *
import datetime
import time
import cPickle as pickle

def get_classes():
    return pickle.load(open('courses.p', 'r'))

def scrape_classes():
    start = time.time()
    term = "201612" #summer term
    schedule = {}
    crawler = ClassScraper()
    subjects = crawler.get_subjects()
    for s in subjects:
        courses = crawler.get_courses(term, s)
        schedule[s] = courses
    #print schedule
    end = time.time()
    print "time for all classes scraped: %r" % (start - end)
    #courses = crawler.get_courses("201612", "CHEM")
    #for c in courses:
    #    c.print_all()
    pickle.dump(schedule, open('courses.p','w'))

#scrape_classes()
schedule = get_classes()

"""
def main():
    #scrape_classes()
    schedule = get_classes()

if __name__ == "__main__":
    main()
"""

'''
start = time.time()
term = "201612" #summer term
schedule = {}
crawler = ClassScraper()
subjects = crawler.get_subjects()
for s in subjects:
    courses = crawler.get_courses(term, s)
    schedule[s] = courses
print schedule
end = time.time()
print "time for all classes scraped: %r" % (start - end)
courses = crawler.get_courses("201612", "CHEM")
for c in courses:
    c.print_all()

current_date = str(datetime.datetime.now())
pickle.dump(courses, open('courses.p','w'))
'''
