from controllers.parameters import ARTICLE
from controllers.parameters import QUESTIONS
from controllers.parameters import OPTIONS
from controllers.parameters import DESCRIPTION
from controllers.parameters import OPTION_NUMBER
from controllers.parameters import TYPE
from controllers.parameters import INSERTED_SENTENCE
from controllers.parameters import HIDE_ARTICLE
from controllers import JSONRequestHandler
from models.common import Section
from models.readings import ReadingSection
from models.listenings import ListeningSection
from models.speakings import SpeakingSection
from models.writings import WritingSection
from django.utils import simplejson as json
from models.common import get_section
from models.test import TestModel
import logging 

class ApiStoreAnswer(JSONRequestHandler):
    
    def post(self, testid, section_type, sectionid, questionid):

        self.response_json({"testid": testid, "sectionid": sectionid, "questionid": questionid, "section_type": section_type})

    def get(self, testid, section_type, sectionid, questionid):
        return self.post(testid, section_type, sectionid, questionid)

   
class ApiGetSection(JSONRequestHandler):

    def get(self, sectionid):
        logging.info("section id is " + sectionid)
        q = Section.all()
        q.filter('sectionid = ', sectionid)
        section = q.get()
        if section:
            self.response_json(section.to_json_str())
        else:
            return
 
class ApiCreateTest(JSONRequestHandler):

    def get(self):
        test_json = json.loads(self.request.get('test'))
        test_model = TestModel.from_dict(test_json)
        test_model.put()
        self.response_json(json.dumps({'result' : "succeed"}))

    def post(self):
        self.get()
        

class ApiCreateSection(JSONRequestHandler):
    '''
    classdocs
    '''

    def post(self):
        json_str = self.request.get('section')
        if not json_str:
            response_json('{"result":"failed"}')
            return

        section_dict = json.loads(json_str)
        if section_dict['type'] == 'reading':
            reading_section = ReadingSection.from_dict(section_dict)
            reading_section.put()
        elif section_dict['type'] == 'listening':
            listening_section = ListeningSection.from_dict(section_dict)
            listening_section.put()
        elif section_dict['type'] == 'speaking':
            speaking_section = SpeakingSection.from_dict(section_dict)
            speaking_section.put()
        elif section_dict['type'] == 'writing':
            writing_section = WritingSection.from_dict(section_dict)
            writing_section.put()
        else: 
            response_json_failed()
        JSONRequestHandler.response_json_succeed(self)
