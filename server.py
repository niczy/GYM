from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from controllers.practice.speaching import SpeachingPage
from controllers.practice.writing import WritingPage
from controllers.practice.reading import ReadingPage
from controllers.practice.listening import ListeningPage
from controllers.home import HomePage
from controllers.signup import SignUp
from controllers.signup import SignUpCheck
from controllers.login import Login
from controllers.login import Logout

'''
Url ruls:

For problem materials:

    / testid / [reading | listening | writing | speaking] / sectionid / 
    Method get, to get the materials for this section.
    For problems may contain multipl materials, the server need to put the extra resource in the returned json, which may point to another resouce whose url must be a sub dir to this url. Because we need to check the access of the user for certain 'testid'

For questions:

    / testid / [reading | listening | writing | speaking] / sectionid / q / id
    Method get, to get the description of a question.
    Method post, to post my answer to put the user's answer to the question

'''
app = webapp.WSGIApplication(
                [('/', HomePage),
                (r'/speaching', SpeachingPage),
                (r'/listening', ListeningPage),
                (r'/(.*)/reading/(.*)', ReadingPage),
                (r'/writing', WritingPage),
                (r'/homepage', HomePage),           
                (r'/signup_check/(.*)', SignUpCheck),
                (r'/signup', SignUp),
                (r'/login', Login),
                (r'/logout', Logout)],
                debug=True)

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
