'''
Created on Dec 6, 2011

@author: charliezhang
'''


from src.controllers.base.output import VisualElement

class Panel(VisualElement):
    def __init__(self, height, width, color):
        VisualElement.__init__(self)
        self.template_values.update({
            'height' : height,
            'width' : width,
            'css_class' : 'panel ' + color,
        })

