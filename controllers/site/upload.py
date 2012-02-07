'''
Created on Jan 12, 2012

@author: charliezhang
'''

from controllers import render_page
from controllers import RequestHandler
from controllers import JSONRequestHandler
from models import utils
from models.common import save_section
from models.listenings import save_listening_section
from models.readings import save_reading_section
from models.utils import TEXT_DATA

class UploadPage(RequestHandler):
    '''
    classdocs
    '''

    def get(self):
        render_page(self, 'upload_page.html', None)

    def post(self):
        xml = self.request.get('xml')
        type = self.request.get('type')
        if xml == None:
            return
        
        sections = utils.xml_to_obj(xml)

        msg = ''
        for section in sections:
            if type == 'listening':
                save_listening_section(section)
                #save_section(section, type)
            elif type == 'reading':
                save_reading_section(section)
            else:
                msg = 'Unknown Type: ' + type
                break
        render_page(self, 'upload_page.html', {"error": msg!='', "error_msg": msg})