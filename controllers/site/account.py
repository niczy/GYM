'''
Created on Dec 28, 2011

@author: charliezhang
'''
from controllers import render_page
from controllers import require_login
from controllers import RequestHandler
from controllers import JSONRequestHandler
import json

class AccountPage(RequestHandler):
    '''
    classdocs
    '''

    @require_login('/landing')
    def get(self):
        #TODO(nice): Get user info for the user: self.username
        username = self.username
        email = 'hhh@123.com'
        credit = 99
        registered_date = '2010-8-1'
        render_page(self, "account_page.html", {
            'username': username,
            'email': email,
            'credit': credit,
            'registered_date': registered_date
            })
        
        
class UserHistoryList(JSONRequestHandler):
    
    @require_login('/landing')
    def get(self):
        #TODO(nice): return a list of tests done by this user: self.username.
        self.response_json(json.dumps({
            "items":[
                {"title": "TPO 1",
                 "testid": 1,
                 "date": "2010-1-2"},
                {"title": "Kanlan 1",
                 "testid": 2,
                 "date": "2010-1-1"}
            ]}));