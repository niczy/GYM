from google.appengine.ext import webapp
from controllers import render_page

class ListeningPage(webapp.RequestHandler):

    def get(self):        
	render_page("listening_page.html", None)
