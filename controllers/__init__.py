import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

TEMPLAGE_DIR = "templates/"
PAGE_DIR = TEMPLAGE_DIR + "pages/"

def render_page(handler, page_name, values):
    username = handler.username
    logged_in = False
    if username:
        logged_in = True

    predefined_values = {
       'logged_in' : logged_in,
       'username' : username
    }
    if values != None:
        predefined_values.update(values)
    handler.response.out.write(template.render(PAGE_DIR + page_name, predefined_values))

def require_login(url):
    def login_check(fn):
        def Get(self, *args):
            self.username = self.request.cookies.get('username')
            if self.username == None and url != None:
                self.redirect(url)
                return
            else:
                fn(self, *args)
        return Get
    return login_check

class RequestHandler(webapp.RequestHandler):
    def __init__(self):
        self.username = ''
        self.template_values = {
        }

    def Render(self, template_path, custom_template_values={}):
        template_values = self.template_values;
        template_values.update(custom_template_values)
        file_path = os.path.join(os.path.dirname(__file__),
                                 os.path.pardir,
                                 os.path.pardir,
                                 'templates',
                                 template_path);
        self.response.out.write(template.render(file_path, template_values))

class JSONRequestHandler(webapp.RequestHandler):
    def __init__(self):
        self.username = ''
        self.template_values = {
        }

    def Response(self, json, type='application/jsonrequest'):
        self.response.headers['Content-Type'] = type
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(json)