'''
Created on Dec 28, 2011

@author: charliezhang
'''
from controllers import render_page
from controllers import require_login
from controllers import RequestHandler
from controllers import JSONRequestHandler
from controllers.site.signup import SignUpCheck
from django.utils import simplejson as json
from google.appengine.api import mail
from models import users

class AccountPage(RequestHandler):
    '''
    classdocs
    '''

    @require_login('/landing')
    def get(self):
        #TODO(nice): Get user info for the user: self.username
        user = users.GetUserByUsernameOrEmail(self.username)
        render_page(self, "account_page.html", {
            'username': user['username'],
            'email': user['email'],
            'credit': user['credit'],
            'registered_date': user['registered_date']
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

class SetNewPassword(RequestHandler):
    def get(self, link, expired=False, error=False, msg=''):
        username = ''
        if expired == False:
            user = users.CheckPasswordResetLink(link)
            if user == None:
                expired = True
            else:
                username = user.username
        render_page(self, "set_password_page.html", {'username': username, 'expired': expired, 'error': error, 'msg': msg})

    def post(self, link):
        user = users.CheckPasswordResetLink(link)
        password = self.request.get('password')
        confirm = self.request.get('confirm')
        expired = False
        error = False
        msg = ''
        if user:
            msg = users.ValidatePassword(password, confirm)
            if not msg:
                users.ResetUserPassword(user, password)
                users.ClearPasswordResetLink(user)
                self.redirect('/login')
            else: 
                error = True
        else:
            expired = True
        self.get(link, expired=expired, error=error, msg=msg)

class ResetPassword(RequestHandler):
    def get(self):
        render_page(self, "get_password_page.html", {'msg': '', 'success': False})
    
    def post(self):
        uoe = self.request.get('uoe')
        user = users.GetUserByUsernameOrEmail(uoe)
        msg = ''
        success = False
        if user == None:
            msg = 'User doesn\'t exist'
        else:
            link = users.CreatePasswordResetLink(user)
            users.SetPasswordResetLink(user, link)
            self.SendPasswordResetEmail(user, link)
            success = True
            msg = 'The password reset link has been sent to you by email.'
        render_page(self, "get_password_page.html", {'msg': msg, 'success': success})

    @staticmethod
    def SendPasswordResetEmail(user, link):
        #TODO(Zero): Change the link to the actual domain
        body = 'Click the following link to reset your password:\n http://localhost:8083/setnewpassword/%s\n' % link
        
        #TODO(Zero): Change to team email address.
        me = 'zero891109@gmail.com'
        you = user.email
        # you == the recipient's email address
        subject = 'Your password on toeflkiller.com'

        mail.send_mail(me, you, subject, body)