'''
Created on Dec 22, 2011

@author: charliezhang
'''
from controllers import RequestHandler
from controllers import render_page

class LandingPage(RequestHandler):
    def get(self):
        render_page(self, "landing_page.html", None)

        