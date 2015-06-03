import requests
import re
from bs4 import BeautifulSoup
from course import *

class ClassScraper:
    def __init__(self):
        #this was gotten off of github; "dummy" is basically an empty form option
        self.term = "201612"
        self.subj = "dummy"
        self.data = [
            ('term_in', self.term),
            ('sel_subj', "dummy"),
            ('sel_day', "dummy"),
            ('sel_schd', "dummy"),
            ('sel_insm', "dummy"),
            ('sel_camp', "dummy"),
            ('sel_levl', "dummy"),
            ('sel_sess', "dummy"),
            ('sel_instr', "dummy"),
            ('sel_ptrm', "dummy"),
            ('sel_attr', "dummy"),
            ('sel_subj', self.subj),
            ('sel_crse', ""),
            ('sel_title', ""),
            ('sel_schd', "%25"),
            ('sel_from_cred', ""),
            ('sel_to_cred', ""),
            ('sel_camp', "%25"),
            ('sel_ptrm', "%25"),
            ('sel_instr', "%25"),
            ('sel_sess', "%25"),
            ('sel_attr', "%25"),
            ('begin_hh', "0"),
            ('begin_mi', "0"),
            ('begin_ap', "a"),
            ('end_hh', "0"),
            ('end_mi', "0"),
            ('end_ap', "a"),
        ]

    def scrape(self):
        information = []
        courses = []
        details = ["(NULL FIELD)","(NULL FIELD)","(NULL FIELD)"]

        str_data = "&".join(["{}={}".format(k, v) for k, v in self.data])
        r = requests.post("https://banssb.fhda.edu/PROD/bwckschd.p_get_crse_unsec",
                           data=str_data)
        soup = BeautifulSoup(r.content)
        for div in soup.find_all({'th':True, 'td':True}, #runs faster as dict with true value
                           attrs={'class':['ddtitle','dddefault']}):
            if div.name == 'th' and div.get('class','') == ['ddtitle']:
                details = div.text.split('-')[0:3]
            else:
                for line in div.descendants:
                    if line.name == 'td' and line.get('class','') == ['dddefault']:
                        try:
                            information.append(str(line.text))
                        except UnicodeEncodeError:
                            information.append("(TBA)")
                        if len(information) == 7:
                            details.extend(information)
                            courses.append(Course(details))
                            information = []
        return courses

    def get_courses(self, term, subj):
        self.data[0] = ('term_in', term)
        self.data[11] = ('sel_subj', subj)
        return self.scrape()

    def get_subjects(self):
        subjects = []
        r = requests.post("https://banssb.fhda.edu/PROD/bwckgens.p_proc_term_date",
                          data={'p_calling_proc': 'bwckschd.p_disp_dyn_sched',
                                'p_term': '201612'})
        soup = BeautifulSoup(r.content)
        for div in soup.find_all('select', attrs={'id':'subj_id'}):
            for subj in div.find_all('option'):
                subjects.append(subj.get('value'))
        return subjects


#class RatingScraper:
