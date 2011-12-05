'''
Created on Dec 5, 2011

@author: charliezhang
'''

import os
import sys

'''
Associate renderer class with its corresponding template file path
'''
class Template():

    file_path_map_ = {
      'HomePage' : 'static_data/templates/homepage.tpl',
    }

    @staticmethod
    def GetFilePath(RendererClass):
        base_dir = sys.path[0];
        return os.path.join(base_dir,
                            Template.file_path_map_.get(RendererClass.__class__.__name__))
    
    def __init__(self):
        '''
        Constructor
        '''
        