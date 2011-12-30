'''
Created on Dec 28, 2011

@author: charliezhang
'''
from controllers import render_page
from controllers import require_login
from controllers import RequestHandler
import json

class UserInfoPage(RequestHandler):
    '''
    classdocs
    '''

    @require_login('/landing')
    def get(self, username):
        #TODO(nice): Get user info for the user: username
        #Note: username is not equal to self.username!
        registered_date = '2010-8-1'
        render_page(self, "userinfo_page.html", {
            'username': username,
            'registered_date': registered_date
            })
