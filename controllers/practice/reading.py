from controllers.parameters import ARTICLE
from controllers.parameters import QUESTIONS
from controllers.parameters import OPTIONS
from controllers.parameters import DESCRIPTION
from controllers.parameters import OPTION_NUMBER
from controllers.parameters import TYPE
from controllers.parameters import INSERTED_SENTENCE
from controllers.parameters import HIDE_ARTICLE
from controllers import render_page
from controllers import RequestHandler
from controllers import JSONRequestHandler
from controllers import require_login
from django.utils import simplejson as json

class ReadingPage(RequestHandler):
    @require_login('/landing')
    def get(self, testid, sectionid):
        self.render_page("reading_page.html", {'testid': testid, "sectionid": sectionid})

