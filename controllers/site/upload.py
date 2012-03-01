'''
Created on Jan 12, 2012

@author: charliezhang
'''

from controllers import render_page
from controllers import RequestHandler
from controllers import JSONRequestHandler
from models import utils
from models.utils import TEXT_DATA

class UploadPage(RequestHandler):
    '''
    classdocs
    '''

    def get(self):
        render_page(self, 'upload_page.html', None)

    def post(self):
        render_page(self, 'upload_page.html', {"error": msg!='', "error_msg": msg})


