'''
Created on Dec 3, 2011

@author: charliezhang
'''

import webapp2

class HomePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Welcome to Toefl-Killer!')
