from google.appengine.ext import webapp

class ReadingPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, this is reading page!')   
