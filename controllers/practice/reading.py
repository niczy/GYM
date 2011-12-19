from controllers import render_page
from controllers import RequestHandler
from controllers import require_login

class ReadingPage(RequestHandler):
    @require_login('/')
    def get(self, testid, sectionid):
        render_page(self, "reading_page.html", {'testid': testid, "sectionid": sectionid})
