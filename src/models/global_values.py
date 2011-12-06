#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Dec 5, 2011

@author: charliezhang
'''
import os
import sys

COLOR_BLUE = 'blue'
COLOR_RED = 'red'
COLOR_YELLOW = 'yellow'
COLOR_GREEN = 'green'
COLOR_BLACK = 'black'
WEBSITE_NAME_EN = 'Toefl-Killer'
WEBSITE_NAME_CN = '托福杀手'


'''
Global static vars used in templates.
'''
class TemplateValues():
    template_values_ = {
        'link_home_page' : '/'
        'link_'
    }
    template_values_en_ = {                   
        'text_home_page_title' : WEBSITE_NAME_EN + ' | Home',

    }
    template_values_cn_ = {
        'text_home_page_title' : WEBSITE_NAME_CN + ' | 首页',     
    }

    @staticmethod
    def Get(*language):
        if len(language) == 1:
            if language[0].upper() == 'EN':
                return TemplateValues.template_values_en_
            elif language[0].upper() == 'CN':
                return TemplateValues.template_values_cn_
        return TemplateValues.template_values_
    
    def __init__(self):
        return

'''
Associate renderer class with its corresponding template file path
'''
class TemplateFilePaths():

    file_path_map_ = {
      'HomePage' : 'static/templates/sitepage/homepage.tpl',
      'Panel' : 'static/templates/sitepage/elements/panel.tpl',
    }

    @staticmethod
    def Get(RendererClass):
        base_dir = sys.path[0];
        return os.path.join(
            base_dir,
            TemplateFilePaths.file_path_map_.get(RendererClass.__class__.__name__))
    
    def __init__(self):
        return