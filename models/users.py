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
def get_user_by_username_or_email(uoe):
    users = db.GqlQuery("SELECT * FROM User WHERE username = :1", uoe)
    for user in users: return user
    users = db.GqlQuery("SELECT * FROM User WHERE email = :1", uoe)
    for user in users: return user
    return None

def get_md5(unhased):
    hashed = hashlib.md5()
    hashed.update(unhased)
    return hashed.hexdigest()
 
 
def user_existed(uoe):
    user = get_user_by_username_or_email(uoe)
    if user == None: return False
    return True

def hash_password(password):
    return get_md5(password + PASSWORD_HASH_KEY)
   
# There should be a deadline for the link.
def set_password_reset_link(user, link):
    user.password_reset_link = link
    user.put()
    pass

# There should be a deadline for the link.
def check_password_reset_link(link):
    if len(link) < 10: return None
    users = db.GqlQuery("SELECT * FROM User WHERE password_reset_link = :1", link)
    for user in users: return user
    return None

def clear_password_reset_link(user):
    user.password_reset_link = ''
    user.put()

def create_password_reset_link(user):
    num = random.random()
    link = get_md5(str(num))
    return link

def reset_user_password(user, password):
    hased_password = hash_password(password)
    user.password = hased_password
    user.put()
   
def valid_username_char(char):
    if char >= 'a' and char <= 'z': return True
    if char >= 'A' and char <= 'Z': return True
    if char == '_': return True
    if char >= '0' and char <= '9': return True
    return False
    
# Register user, return error message if failed. return None if success
def register_user(username, email, password, confirm):
    if password != confirm:
        return 'Password and confirm not equal!'
    msg = validate_username(username)
    if msg: return msg
    msg = validate_password(password, confirm)
    if msg: return msg
    if user_existed(username):
        return 'Username had been used!'
    if user_existed(email):
        return 'Email had been used!'  
    hashed_password = hash_password(password)
    user = User(username=username,
               email=email,
               password=hashed_password,
               register_date=datetime.datetime.now().date(),
               credit=0)
    user.put()
    return None #Success!

def get_user_cookie_key(uoe):
    hashed = hashlib.md5()
    hashed.update(USER_COOKIE_HASH_KEY + uoe)
    return hashed.hexdigest()
    
def login_with_username_or_email(handler, uoe, password):
    hashed_password = hash_password(password)
    user = get_user_by_username_or_email(uoe)
    if user and user.password == hashed_password:
        cookie_key = get_user_cookie_key(user.username)
        handler.response.headers.add_header('Set-Cookie','username=' + user.username + '; expires=Sun, 31-May-2999 23:59:59 GMT; path=/;')
        handler.response.headers.add_header('Set-Cookie','key=' + cookie_key + '; expires=Sun, 31-May-2999 23:59:59 GMT; path=/;')
        return None #Success!
    return 'Username/email Don''t exist or password is wrong!' #Failed!

def validate_username(username):
    if len(username) < 4:
        return 'Username Too Short! At least 4 characters'
    if len(username) > 20:
        return 'Username Too Long! At most 20 characters'
    for c in username:
        if not valid_username_char(c):
            return 'Must consists of english charactors, underscore or digits'
    if get_user_by_username_or_email(username):
        return 'User Existed!'
    return None

def validate_password(password, confirm):
    if password != confirm:
        return "Password and confirmation are not equal! Please check again"
    if len(password) < 6:
        return "Password too short. At least 6 characters"
    
    return None
    
def validate_email(email):
    if not re.match(".+@.+\..+", email):
        return 'Email wrong format!'
    if get_user_by_username_or_email(email):
        return 'Email already in use!'
    return None