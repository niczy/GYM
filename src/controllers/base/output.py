'''
Created on Dec 6, 2011

@author: charliezhang
'''

from google.appengine.ext.webapp import template
from src.models.global_values import TemplateFilePaths

'''
Base class for Visual Elements

Visual Elements should derive from this base class.
Derived classes set up self.template_vales, 
The base class's RenderElement() method will return html content.
'''
class VisualElement():
    def __init__(self):
        self.template_values = {
            'aaa' : 'bbb'
        }

    def Render(self):
        self.path = TemplateFilePaths.Get(self)
        return template.render(self.path, self.template_values)