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
        
        msg = SignUpCheck.ValidateUsername(username)
        if msg: return msg
        msg = SignUpCheck.ValidatePassword(password, confirm)
        if msg: return msg
        return None   
        
    
class SignUpCheck(JSONRequestHandler):
    def get(self, check_field):
        pass
    
    def post(self, check_field):
        #TODO(nice): Validate username and email, length/RE/existed
        value = self.request.get('value')
        result = ''
        if check_field == 'username':
            result = SignUpCheck.ValidateUsername(value)
            if not result:
                result = 'good'

        elif check_field == 'email':
            result = 'good'
        self.response_json(result, 'text/plain');
    
    #TODO(nice): Username validation. Return None if it's valid, else return error message
    @staticmethod
    def ValidateUsername(username):
        if len(username) < 4:
            return 'Username Too Short! At least 4 characters'
        return None
    
    #TODO(nice): Password validation. Return None if it's valid, else return error message
    @staticmethod
    def ValidatePassword(password, confirm):
        if password != confirm:
            return "Password and confirmation are not equal! Please check again"
        if len(password) < 6:
            return "Password too short. At least 6 characters"
        return None
    
        