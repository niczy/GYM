'''
Created on Dec 3, 2011

@author: charliezhang
'''

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from models.predefined_template_values import GlobalValues
from models.template_file_paths import Template


class HomePage(webapp.RequestHandler):
    def get(self):
        template_values = GlobalValues.TemplateValues('CN');
        
        # description = 'This page is generated from a template!'
        template_values.update({
        #    'description': description,
        })

        path = Template.GetFilePath(self)
        self.response.out.write(template.render(path, template_values))
        

