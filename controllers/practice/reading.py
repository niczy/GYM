from controllers import render_page
from controllers import RequestHandler

class ReadingPage(RequestHandler):

    def get(self):
        render_page(self, "reading_page.html", None)
