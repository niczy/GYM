'''
Created on Dec 10, 2011

@author: charliezhang
'''

from controllers.base.handlers import RequestHandler
from models.data_types import User

class SignUp(RequestHandler):
    def get(self):
        self.Render('pages/signup_page.html')
    
    def post(self):
        pass