'''
Created on Dec 10, 2011

@author: charliezhang
'''

from src.controllers.base.handlers import RequestHandler
from src.models.data_types import User
from src.models.data_proxy import DataProxy

class SignUp(RequestHandler):
    def get(self):
        self.RenderPage()
    
    def post(self):
        user = User();
        user.username = self.request.get('username');
        user.email = self.request.get('email');
        user.password = self.request.get('password');
        if DataProxy.GetUserByUsername(user.username):
            self.response.out.write('Failed! Username existed: ' + user.username);
            return
        if DataProxy.GetUserByEmail(user.email):
            self.response.out.write('Failed! Email already used: ' + user.email);
            return
        result = DataProxy.RegisterUser(user);
        if result:
            self.response.out.write('Success!');
        else:
            self.response.out.write('Failed!');