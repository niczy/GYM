'''
Created on Dec 3, 2011

@author: charliezhang
'''
from google.appengine.ext import webapp
from controllers import render_page

class HomePage(webapp.RequestHandler):
    def get(self):
	render_page(self, "home_page.html", None)
