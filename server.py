from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from controllers.speaching import SpeachingPage
from controllers.writing import WritingPage
from controllers.reading import ReadingPage
from controllers.listening import ListeningPage
from controllers.homepage import HomePage


class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')

app = webapp.WSGIApplication(
                [('/', MainPage),
                (r'/speaching', SpeachingPage),
                (r'/listening', ListeningPage),
                (r'/reading', ReadingPage),
                (r'/writing', WritingPage),
                (r'/homepage', HomePage)],
                debug=True)

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
