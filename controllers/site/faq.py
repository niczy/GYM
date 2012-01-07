'''
Created on Dec 23, 2011

@author: charliezhang
'''
from controllers import render_page
from controllers import require_login
from controllers import RequestHandler
from controllers import JSONRequestHandler
from controllers.parameters import ANONYMOUS_USER
from django.utils import simplejson as json

import datetime
from google.appengine.ext import db

class ModelFaq(db.Model):
    username = db.StringProperty(required=True)
    question = db.StringProperty(required=True)
    answer = db.StringProperty(required=False)
    post_date = db.DateProperty()

def PostFaq(username, question):
    faq = ModelFaq(username=username,
                   question=question,
                   post_date=datetime.datetime.now().date())
    faq.put()

def GetFaqList():
    return db.GqlQuery("SELECT * FROM ModelFaq ORDER BY post_date DESC")

def DatetimeToString(date):
    return datetime.datetime.strftime(date, "%Y-%m-%d")
    
class FAQPage(RequestHandler):
    '''
    classdocs
    '''
    @require_login(None)
    def get(self):
        render_page(self, "faq.html", None)


    @require_login(None)
    def post(self):
        question = self.request.get('question')
        anonymous = (self.request.get('anonymous') == 'on')
        #TODO(nice): Save a Q&A posted my user. {question: question, username: self.username}
        # if anonymous, save a constant username for anonymous users.
        username = self.username
        if username == None or anonymous:
            username = 'Anonymous'
        PostFaq(username, question)
        self.redirect('/faq')
        
class FAQList(JSONRequestHandler):
    def get(self):
        #TODO(nice):return a list of Q&A as following: in reverse-time order.
        faqList = GetFaqList()
        items = []
        for faq in faqList:
            answer = faq.answer
            if answer == None:
                answer = 'No answer yet.'
            items.append({'question':faq.question,
                          'answer': answer,
                          'user': faq.username,
                          'date': DatetimeToString(faq.post_date)
                         })
            
        self.response_json(json.dumps({'items':items}))
        return
        self.response_json(json.dumps({
            "items":[
                {"question": "Who is the richest guy?",
                 "answer": "Nic",
                 "user": ANONYMOUS_USER,
                 "date": "2010-1-2"},
                {"question": "What is the greatest game?",
                 "answer": "DotA",
                 "user": "drizzlecrj",
                 "date": "2010-1-1"}
            ]}));

        
        