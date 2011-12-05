#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Dec 5, 2011

@author: charliezhang
'''

'''
Global static vars used in templates.
'''
class GlobalValues():
    template_values_ = {
        'home_page_link' : '/'
    }
    template_values_en_ = {                   
        'home_page_title' : 'Toelf-Killer | Home',     
    }
    template_values_cn_ = {
        'home_page_title' : '托福杀手 | 首页',     
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