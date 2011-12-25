'''
Created on Dec 23, 2011

@author: charliezhang
'''
from controllers import render_page
from controllers import require_login
from controllers import RequestHandler
from controllers import JSONRequestHandler

class FeedBackPage(RequestHandler):
    '''
    classdocs
    '''
    @require_login(None)
    def get(self):
        render_page(self, "feedback.html", None)