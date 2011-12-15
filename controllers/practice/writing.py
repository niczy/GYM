from google.appengine.ext import webapp
from controllers import render_page

class WritingPage(webapp.RequestHandler):

    def get(self):
	render_page("wriging_page.html", None)
