from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from src.controllers.testpage.speaching import SpeachingPage
from src.controllers.testpage.writing import WritingPage
from src.controllers.testpage.reading import ReadingPage
from src.controllers.testpage.listening import ListeningPage
from src.controllers.sitepape.homepage import HomePage

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
