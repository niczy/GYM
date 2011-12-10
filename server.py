from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from controllers.practice.speaching import SpeachingPage
from controllers.practice.writing import WritingPage
from controllers.practice.reading import ReadingPage
from controllers.practice.listening import ListeningPage
from controllers.home import HomePage

app = webapp.WSGIApplication(
                [('/', HomePage),
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
