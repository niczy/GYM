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

    def Render(self, template_path, template_values={}):
        file_path = os.path.join(os.path.dirname(__file__),
                                 os.path.pardir,
                                 os.path.pardir,
                                 'templates',
                                 template_path);
        self.response.out.write(template.render(file_path, template_values))