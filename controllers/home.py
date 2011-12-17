'''
Created on Dec 3, 2011

@author: charliezhang
'''
from controllers import render_page
from controllers import require_login
from controllers import RequestHandler

class HomePage(RequestHandler):
    @require_login(None)
    def get(self):
	    render_page(self, "home_page.html", None)
