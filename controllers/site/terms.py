'''
Created on Dec 15, 2011

@author: charliezhang
'''
from controllers import RequestHandler

class TermsOfUse(RequestHandler):
    '''
    classdocs
    '''


    def get(self):
        self.Render('pages/terms_of_use.html')