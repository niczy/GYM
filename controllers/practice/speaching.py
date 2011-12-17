from controllers import render_page
from controllers import RequestHandler

class SpeachingPage(RequestHandler):

    def get(self):
	    render_page(self, "listening_page.html", None)
