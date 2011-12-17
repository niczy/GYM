from controllers import render_page
from controllers import RequestHandler

class WritingPage(RequestHandler):

    def get(self):
	    render_page(self, "writing_page.html", None)
