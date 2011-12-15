from google.appengine.ext import webapp
from controllers import render_page

class ReadingPage(webapp.RequestHandler):

    def get(self):
        render_page("reading_page.html", None)
