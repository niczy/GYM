'''
Created on Dec 16, 2011

@author: charliezhang
'''

from controllers import render_page
from controllers import RequestHandler

class Login(RequestHandler):
    def get(self):
        render_page(self, 'login_page.html', {'error':False});
        
    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        error = Login.LogInWithUsernameOrEmail(self, username, password)
        if not error:
            self.redirect("/")
        else:
            render_page(self, 'login_page.html',{'error':True,
                                             'error_msg':error});
    
    @staticmethod
    def LogInWithUsernameOrEmail(handler, username, password):
        #TODO(nice): Implement log in check. (username/password)
        if (username == 'Zero' or username == 'zero@g.com') and password == '123':
            #TODO(zero): Escape username 
            handler.response.headers.add_header('Set-Cookie','username=' + username + '; expires=Sun, 31-May-2999 23:59:59 GMT; path=/;')
            #self.response.set_cookie('usrename', username, max_age=99999999, path='/', secure=True)
            #self.response.headers['Set-Cookie']
            return None
        
        return 'Username Don''t exist'

class Logout(RequestHandler):
    def get(self):
        self.response.headers.add_header('Set-Cookie','username=''; expires=Sun, 31-May-1999 23:59:59 GMT; path=/;')
        self.redirect('/')