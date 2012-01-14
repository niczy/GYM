'''
Created on Dec 16, 2011

@author: charliezhang
'''

from controllers import render_page
from controllers import RequestHandler
from models import users

class Login(RequestHandler):
    def get(self):
        render_page(self, 'login_page.html', {'error':False});
        
    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        error = users.login_with_username_or_email(self, username, password)
        if not error:
            self.redirect("/")
        else:
            render_page(self, 'login_page.html',{'error':True,
                                             'error_msg':error});

class Logout(RequestHandler):
    def get(self):
        self.response.headers.add_header('Set-Cookie','username=''; expires=Sun, 31-May-1999 23:59:59 GMT; path=/;')
        self.redirect('/')