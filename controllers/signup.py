'''
Created on Dec 10, 2011

@author: charliezhang
'''

from controllers.base.handlers import RequestHandler
from controllers.base.handlers import JSONRequestHandler
from models.data_types import User

class SignUp(RequestHandler):
    def get(self):
        self.Render('pages/signup_page.html')
    
    def post(self):
        username = self.request.get('username')
        email = self.request.get('email')
        password = self.request.get('password')
        confirm = self.request.get('confirm')
        if username and email and password and confirm and \
        SignUpCheck.ValidUsername(username) and confirm == password:
            self.response.out.write("Success!")
        else:
            self.response.out.write("Failed!")
            
        
    
class SignUpCheck(JSONRequestHandler):
    def get(self, check_field):
        pass
    
    def post(self, check_field):
        value = self.request.get('value')
        result = ''
        if check_field == 'username':
            if SignUpCheck.ValidUsername(value):
                result = 'good'
            else:
                result = 'User name too short!'
            
        elif check_field == 'email':
            result = 'good'
        self.Response(result);
    
    @staticmethod
    def ValidUsername(username):
        return len(username) > 3
        