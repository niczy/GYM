from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class ReadingPage(webapp.RequestHandler):

    def get(self):
        self.response.out.write(template.render("templates/pages/reading_page.html", None))
