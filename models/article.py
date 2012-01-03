from google.appengine.ext import db

class Article(db.Model):
    testid = db.IntegerProperty()
    sectionid = db.IntegerProperty()
    content = db.TextProperty()


