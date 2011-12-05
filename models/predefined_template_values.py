#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Dec 5, 2011

@author: charliezhang
'''

WEBSITE_NAME_EN = 'Toefl-Killer'
WEBSITE_NAME_CN = '托福杀手'

'''
Global static vars used in templates.
'''
class GlobalValues():
    template_values_ = {
        'link_home_page' : '/'
    }
    template_values_en_ = {                   
        'text_home_page_title' : WEBSITE_NAME_EN + ' | Home',

    }
    template_values_cn_ = {
        'text_home_page_title' : WEBSITE_NAME_CN + ' | 首页',     
    }

    @staticmethod
    def TemplateValues(*language):
        if len(language) == 1:
            if language[0].upper() == 'EN':
                return GlobalValues.template_values_en_
            elif language[0].upper() == 'CN':
                return GlobalValues.template_values_cn_
        return GlobalValues.template_values_
    
    def __init__(self):
        return