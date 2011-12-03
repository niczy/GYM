'''
Created on Dec 3, 2011

@author: charliezhang
'''

from google.appengine.ext import webapp

class HomePage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Welcome to Toefl-Killer!')
