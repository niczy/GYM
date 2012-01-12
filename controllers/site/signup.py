'''
Created on Dec 10, 2011

@author: charliezhang
'''

from controllers import render_page
from controllers import RequestHandler
from controllers import JSONRequestHandler
from models import users
from controllers.site.login import Login

class SignUp(RequestHandler):
    def get(self):
        render_page(self, 'signup_page.html', {'error' : False})
    
    def post(self):
        
        username = self.request.get('username')
        email = self.request.get('email')
        password = self.request.get('password')
        confirm = self.request.get('confirm')
        msg = users.register_user(username, email, password, confirm)
        if msg:
            render_page(self, 'signup_page.html', {'error' : True,
                                                   'error_msg' : msg,
                                                   'username' : username,
                                                   'email': email})
            return
        msg = users.login_with_username_or_email(self, username, password)
        if not msg:
            self.redirect('/');
        else:
            self.redirect('/login')
           
class SignUpCheck(JSONRequestHandler):
    def get(self, check_field):
        pass
    
    def post(self, check_field):
        value = self.request.get('value')
        result = ''
        if check_field == 'username':
            result = users.validate_username(value)
            if not result:
                result = 'good'

        elif check_field == 'email':
            result = users.validate_email(value)
            if not result:
                result = 'good'
        self.response_json(result, 'text/plain');
    

    
        