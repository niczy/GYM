import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from models import users

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
            if self.username:
                key = self.request.cookies.get('key')
                expected_key = users.get_user_cookie_key(self.username)
                if key != expected_key:
                    self.username = None
                    
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

    def render_page(self, page_name, custom_template_values={}):
        template_values = self.template_values;
        template_values.update(custom_template_values)
        self.response.out.write(template.render(PAGE_DIR + page_name, template_values))

class JSONRequestHandler(webapp.RequestHandler):
    def __init__(self):
        self.username = ''
        self.template_values = {
        }

    def response_json(self, json, type='application/json'):
        self.response.headers['Content-Type'] = type
        self.response.out.write(json)

    def response_json_failed(self, msg = None):
        if msg:
            self.response_json('{"result":"failed", "msg": %s}', msg)
        else:
            self.response_json('{"result":"failed"}')

    def response_json_succeed(self):
        self.response_json('{"result":"succeed"}')

