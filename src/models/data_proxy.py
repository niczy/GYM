'''
Created on Dec 10, 2011

@author: charliezhang
'''

from google.appengine.ext import db
from src.models import data_types;

DATA_STORE = "DATA_STORE"


class DataProxy():

    def __init__(self, backend):
        self.back_end = backend;
           
    # Return User if the username exists, otherwise empty.
    @staticmethod
    def GetUserByUsername(username):
        users = db.GqlQuery("SELECT * "
                            "FROM User "
                            "WHERE username = :1 ",
                            username)
        for user in users:
            return user
        return None
    
    # Return User if the email exists, otherwise empty.
    @staticmethod
    def GetUserByEmail(email):
        users = db.GqlQuery("SELECT * "
                            "FROM User "
                            "WHERE email = :1 ",
                            email)
        for user in users:
            return user
        return None
    
    # Return true iff register succeed.
    @staticmethod
    def RegisterUser(user):
        user.put()
        return True
        
        