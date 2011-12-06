'''
Created on Dec 3, 2011

@author: charliezhang
'''

from src.controllers.base.handlers import RequestHandler

class HomePage(RequestHandler):
    def get(self):
        description = 'Author: Zero'
        self.template_values.update({
            'description': description,
        })
        self.RenderPage()

