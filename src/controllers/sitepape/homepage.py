'''
Created on Dec 3, 2011

@author: charliezhang
'''

from src.models import global_values
from src.controllers.base.handlers import RequestHandler
from src.controllers.sitepape.elements.panels import Panel

class HomePage(RequestHandler):
    def get(self):
        description = 'Author: Zero'
        self.template_values.update({
            'description': description,
            'panel_1' : Panel('200', '200', global_values.COLOR_BLUE).Render(),
            'panel_2' : Panel('100', '400', global_values.COLOR_GREEN).Render(),
            'panel_3' : Panel('400', '100', global_values.COLOR_BLACK).Render(),
        })
        self.RenderPage()

