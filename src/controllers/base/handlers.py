'''
Created on Dec 6, 2011

@author: charliezhang

Description:
Base handlers for the website.
'''

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from src.models.global_values import TemplateValues
from src.models.global_values import TemplateFilePaths

class RequestHandler(webapp.RequestHandler):
    def __init__(self):
        self.template_values = TemplateValues.Get()
        
    def CheckAccessibility(self):
        todo = 1 #TODO
        
    def RenderPage(self):
        self.path = TemplateFilePaths.Get(self)
        self.response.out.write(template.render(self.path, self.template_values))