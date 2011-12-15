'''
Created on Dec 3, 2011

@author: charliezhang
'''
from controllers.base.handlers import RequestHandler

class HomePage(RequestHandler):
    def get(self):
        self.response.out.write("Main page") 
