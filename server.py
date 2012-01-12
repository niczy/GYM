import os
import os.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from google.appengine.dist import use_library
use_library('django', '1.2')

from django.conf import settings

settings.configure(INSTALLED_APPS=('nothing',))

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from controllers.practice.speaching import SpeachingPage
from controllers.practice.writing import WritingPage
from controllers.practice.reading import ReadingPage
from controllers.practice.reading import ApiGetReadingSection
from controllers.practice.listening import ListeningPage
from controllers.practice.common_api import ApiStoreAnswer
from controllers.practice.common_api import ApiGetSection
from controllers.practice.common_api import ApiGetSectionById
from controllers.site.home import HomePage
from controllers.site.home import TestMenu
from controllers.site.home import TestDetail
from controllers.site.home import TestHistoryList
from controllers.site.account import AccountPage
from controllers.site.account import ResetPassword
from controllers.site.account import SetNewPassword
from controllers.site.account import UserHistoryList
from controllers.site.userinfo import UserInfoPage
from controllers.site.signup import SignUp
from controllers.site.signup import SignUpCheck
from controllers.site.login import Login
from controllers.site.login import Logout
from controllers.site.landing import LandingPage
from controllers.site.upload import UploadPage
from controllers.site.practice import PracticeMenuPage
from controllers.site.practice import PracticeMenu
from controllers.site.faq import FAQPage
from controllers.site.faq import FAQList
from controllers.site.feedback import FeedBackPage

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
                (r'/api/update_answer/(.*)/(reading|writing|speaking|listening)/(.*)/(.*)', ApiStoreAnswer),

                (r'/api/get/(.*)/(reading|writing|speaking|listening)/(.*)', ApiGetSection),
                (r'/api/getsectionbyid/(.*)', ApiGetSectionById),
                (r'/speaching', SpeachingPage),
                (r'/listening', ListeningPage),
                (r'/(.*)/reading/(.*)/', ReadingPage),
                (r'/landing', LandingPage),
                (r'/writing', WritingPage),
                (r'/homepage', HomePage),           
                (r'/signup_check/(.*)', SignUpCheck),
                (r'/signup', SignUp),
                (r'/login', Login),
                (r'/logout', Logout),
                (r'/api/testmenu', TestMenu),
                (r'/api/practicemenu', PracticeMenu),
                (r'/api/faqlist', FAQList),
                (r'/api/testhistory', TestHistoryList),
                (r'/api/userhistory', UserHistoryList),
                (r'/practices', PracticeMenuPage),
                (r'/faq', FAQPage),
                (r'/feedback', FeedBackPage),
                (r'/testdetail/(.*)', TestDetail),
                (r'/account', AccountPage),
                (r'/userinfo/(.*)', UserInfoPage),
                (r'/resetpassword', ResetPassword),
                (r'/setnewpassword/(.*)', SetNewPassword),
                (r'/upload', UploadPage)],
                debug=True)

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
