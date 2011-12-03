import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from controllers.speaching import SpeachingPage
from controllers.writing import WritingPage
from controllers.reading import ReadingPage
from controllers.listening import ListeningPage


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')

app = webapp2.WSGIApplication(
                [('/', MainPage),
                (r'/speaching', SpeachingPage),
                (r'/listening', ListeningPage),
                (r'/reading', ReadingPage),
                (r'/writing', WritingPage)],
                debug=True)
