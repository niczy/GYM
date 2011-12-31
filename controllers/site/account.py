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
#TODO(nice): Get user's info by username or email.
# Move this method to a proper place.
#return None if not found
def GetUserByUsernameOrEmail(uoe):
    return {'username': uoe,
            'email': 'zero891109@gmail.com',
            'credit': 99,
            'registered_date': '2010-8-1' }

#TODO(nice): Save the password Reset link in user's Database.
# There should be a deadline for the link.
def SetPasswordResetLink(user, link):
    pass

#TODO(nice): Check if the Reset link is correct. If true return the user, else return None
# There should be a deadline for the link.
def CheckPasswordResetLink(link):
    if link == '1357QWERT':
        return {'username': 'drizzlecrj'}
    else:
        return None

#TODO(nice): Create a password Reset link for the user.
def CreatePasswordResetLink(user):
    link = '1357QWERT'
    SetPasswordResetLink(user, link)
    return link

#TODO(nice): Reset user password
def ResetUserPassword(user, password):
    pass

class AccountPage(RequestHandler):
    '''
    classdocs
    '''

    @require_login('/landing')
    def get(self):
        #TODO(nice): Get user info for the user: self.username
        user = GetUserByUsernameOrEmail(self.username)
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
            user = CheckPasswordResetLink(link)
            if user == None:
                expired = True
            else:
                username = user['username']
        render_page(self, "set_password_page.html", {'username': username, 'expired': expired, 'error': error, 'msg': msg})

    def post(self, link):
        user = CheckPasswordResetLink(link)
        password = self.request.get('password')
        confirm = self.request.get('confirm')
        expired = False
        error = False
        msg = ''
        if user:
            msg = SignUpCheck.ValidatePassword(password, confirm)
            if not msg:
                ResetUserPassword(user, password)
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
        email = self.request.get('email')
        user = GetUserByUsernameOrEmail(email)
        msg = ''
        success = False
        if user == None:
            msg = 'User doesn\'t exist'
        else:
            link = CreatePasswordResetLink(user)
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
        you = user['email']
        # you == the recipient's email address
        subject = 'Your password on toeflkiller.com'

        mail.send_mail(me, you, subject, body)