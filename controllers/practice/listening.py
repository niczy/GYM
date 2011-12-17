from controllers import render_page
from controllers import require_login
from controllers import RequestHandler

class ListeningPage(RequestHandler):

    @require_login('/')
    def get(self):
	    render_page(self, "listening_page.html", None)
