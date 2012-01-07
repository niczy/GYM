'''
Created on Dec 10, 2011

@author: charliezhang
'''
from google.appengine.ext import db
import datetime
import hashlib
import re
import random

PASSWORD_HASH_KEY = "THISISARANDOMSEQUENCE4108s981sdnvSKJFN192"
USER_COOKIE_HASH_KEY = "THISISANOTHERRANDOMSEQUENCE23498q823jhfZKJFDQS"


class User(db.Model):
    username = db.StringProperty(indexed=True);
    email = db.StringProperty(indexed=True);
    password = db.StringProperty(required=True);
    register_date = db.DateProperty();
    credit = db.IntegerProperty(required=True);
    password_reset_link = db.StringProperty(indexed=True);

#Get user's info by username or email.
#return None if not found
def GetUserByUsernameOrEmail(uoe):
    users = db.GqlQuery("SELECT * FROM User WHERE username = :1", uoe)
    for user in users: return user
    users = db.GqlQuery("SELECT * FROM User WHERE email = :1", uoe)
    for user in users: return user
    return None

def MD5(unhased):
    hashed = hashlib.md5()
    hashed.update(unhased)
    return hashed.hexdigest()
 
 
def UserExisted(uoe):
    user = GetUserByUsernameOrEmail(uoe)
    if user == None: return False
    return True

def HashPassword(password):
    return MD5(password + PASSWORD_HASH_KEY)
   
# There should be a deadline for the link.
def SetPasswordResetLink(user, link):
    user.password_reset_link = link
    user.put()
    pass

# There should be a deadline for the link.
def CheckPasswordResetLink(link):
    users = db.GqlQuery("SELECT * FROM User WHERE password_reset_link = :1", link)
    for user in users: return user
    return None

def ClearPasswordResetLink(user):
    user.password_reset_link = ''
    user.put()

def CreatePasswordResetLink(user):
    num = random.random()
    link = MD5(str(num))
    return link

def ResetUserPassword(user, password):
    hased_password = HashPassword(password)
    user.password = hased_password
    user.put()
   
def ValidUsernameChar(char):
    if char >= 'a' and char <= 'z': return True
    if char >= 'A' and char <= 'Z': return True
    if char == '_': return True
    if char >= '0' and char <= '9': return True
    return False
    
# Register user, return error message if failed. return None if success
def RegisterUser(username, email, password, confirm):
    if password != confirm:
        return 'Password and confirm not equal!'
    msg = ValidateUsername(username)
    if msg: return msg
    msg = ValidatePassword(password, confirm)
    if msg: return msg
    if UserExisted(username):
        return 'Username had been used!'
    if UserExisted(email):
        return 'Email had been used!'  
    hashed_password = HashPassword(password)
    user = User(username=username,
               email=email,
               password=hashed_password,
               register_date=datetime.datetime.now().date(),
               credit=0)
    user.put()
    return None #Success!

def LogInWithUsername(username, hashed_password):
    users = db.GqlQuery("SELECT * FROM User WHERE username = :1 AND password = :2", username, hashed_password)
    user = users.get()
    if not user: return False
    return True

def LogInWithEmail(email, hashed_password):
    users = db.GqlQuery("SELECT * FROM User WHERE email = :1 AND password = :2", email, hashed_password)
    user = users.get()
    if not user: return False
    return True

def GetUserCookieKey(uoe):
    hashed = hashlib.md5()
    hashed.update(USER_COOKIE_HASH_KEY + uoe)
    return hashed.hexdigest()
    
def LogInWithUsernameOrEmail(handler, uoe, password):
    hashed_password = HashPassword(password)
    if LogInWithUsername(uoe, hashed_password) or LogInWithEmail(uoe, hashed_password):
        cookie_key = GetUserCookieKey(uoe)
        handler.response.headers.add_header('Set-Cookie','username=' + uoe + '; expires=Sun, 31-May-2999 23:59:59 GMT; path=/;')
        handler.response.headers.add_header('Set-Cookie','key=' + cookie_key + '; expires=Sun, 31-May-2999 23:59:59 GMT; path=/;')
        return None #Success!
    return 'Username/email Don''t exist or password is wrong!' #Failed!

def ValidateUsername(username):
    if len(username) < 4:
        return 'Username Too Short! At least 4 characters'
    if len(username) > 20:
        return 'Username Too Long! At most 20 characters'
    for c in username:
        if not ValidUsernameChar(c):
            return 'Must consists of english charactors, underscore or digits'
    return None

def ValidatePassword(password, confirm):
    if password != confirm:
        return "Password and confirmation are not equal! Please check again"
    if len(password) < 6:
        return "Password too short. At least 6 characters"
    return None
    
def ValidateEmail(email):
    return None