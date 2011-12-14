'''
Created on Dec 6, 2011

@author: charliezhang

Description:
Base handlers for the website.
'''

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class RequestHandler(webapp.RequestHandler):
    def __init__(self):
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
        self.template_values = {
        }

    def Response(self, json):
        #self.response.headers['Content-Type'] = 'application/jsonrequest'
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(json)