'''
Created on Dec 6, 2011

@author: charliezhang

Description:
Base handlers for the website.
'''

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from src.models.predefined_template_values import GlobalValues
from src.models.template_file_paths import TemplatePathFinder

class RequestHandler(webapp.RequestHandler):
    def __init__(self):
        self.template_values = GlobalValues.TemplateValues()
        
    def CheckAccessibility(self):
        todo = 1 #TODO
        
    def RenderPage(self):
        path = TemplatePathFinder.GetFilePath(self)
        self.response.out.write(template.render(path, self.template_values))