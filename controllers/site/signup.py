'''
Created on Dec 10, 2011

@author: charliezhang
'''

from controllers import render_page
from controllers import RequestHandler
from controllers import JSONRequestHandler
from models.data_types import User
from controllers.site.login import Login

class SignUp(RequestHandler):
    def get(self):
        render_page(self, 'signup_page.html', {'error' : False})
    
    def post(self):
        
        username = self.request.get('username')
        email = self.request.get('email')
        password = self.request.get('password')
        confirm = self.request.get('confirm')
        msg = SignUp.RegisterUser(username, email, password, confirm)
        if not msg:
            msg = Login.LogInWithUsernameOrEmail(self, username, password)
        if not msg:
            self.redirect('/');
        else:
            render_page(self, 'signup_page.html', {'error' : True,
                                                   'error_msg' : msg})

    @staticmethod
    def RegisterUser(username, email, password, confirm):
        #TODO(nice): Register user, return error message. return None if success
        if username and email and password and confirm and \
        SignUpCheck.ValidUsername(username) and confirm == password:
            return None
        else:
            return "Register Failed!"       
        
    
class SignUpCheck(JSONRequestHandler):
    def get(self, check_field):
        pass
    
    def post(self, check_field):
        #TODO(nice): Validate username and email, length/RE/existed
        value = self.request.get('value')
        result = ''
        if check_field == 'username':
            if SignUpCheck.ValidUsername(value):
                result = 'good'
            else:
                result = 'User name too short!'
            
        elif check_field == 'email':
            result = 'good'
        self.response_json(result, 'text/plain');
    
    @staticmethod
    def ValidUsername(username):
        return len(username) > 3
    
    
        