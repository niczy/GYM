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
        anonymos = (self.request.get('anonymous') == 'on')
        #TODO(nice): Save a Q&A posted my user. {question: question, username: self.username}
        # if anonymous, save a constant username for anonymous users.
        self.redirect('/faq')
        
class FAQList(JSONRequestHandler):

    def get(self):
        #TODO(nice):return a list of Q&A as following: in reverse-time order.
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

        
        