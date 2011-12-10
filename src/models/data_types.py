'''
Created on Dec 10, 2011

@author: charliezhang
'''
from google.appengine.ext import db

class User(db.Model):
    username = db.StringProperty(indexed=True);
    email = db.StringProperty(indexed=True);
    password = db.StringProperty();