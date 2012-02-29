from controllers.parameters import ARTICLE
from controllers.parameters import QUESTIONS
from controllers.parameters import OPTIONS
from controllers.parameters import DESCRIPTION
from controllers.parameters import OPTION_NUMBER
from controllers.parameters import TYPE
from controllers.parameters import INSERTED_SENTENCE
from controllers.parameters import HIDE_ARTICLE
from controllers import JSONRequestHandler
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

class ApiGetSectionById(JSONRequestHandler):
    def get(self, sectionid):
        section = get_section(sectionid)
        if section == None: return
        self.response_json(json.dumps(section))
    
class ApiGetSection(JSONRequestHandler):

    def get(self, testid, section_type, sectionid):
        logging.info('test id is ' + testid)
        logging.info('section type is ' + section_type)
        logging.info('section id is' + sectionid)

        self.response_json(json.dumps({
                                        ARTICLE:["Googe is a <gym reference-id='0' type='highlight'>sexual</gym> act originating in the Amazon <gym reference-id='2'></gym>rainforest. It is where the man wraps <gym reference-id='2'></gym>his legs around a womans face and googe's like a bad badger. It is now used as an exclamation of hornyness or used as a term instead of fuck, or also c", 'formerly known as Google, the new name Googe was implemented on the 14th of February 2007 (Valentines day) with a chocolate covered strawberry kicking ou', "Originated as a typo on the Google homepage, on Feb 14 of 2007 its was supposed to be a special <gym reference-id='1'>valentines day</gym> Google loge, but the artist misspelled Google. "], 
                                        QUESTIONS:[{
                                                DESCRIPTION: "This is the question description1", 
                                                OPTIONS: ['this is an option', 'option2', 'option3', 'option4'], TYPE: 0
                                                    
                                                    },
                                                    
                                                    { DESCRIPTION: " the question description2", 
OPTIONS: ['option1', 'option2', 'option3', 'option4'], OPTION_NUMBER: 2, TYPE: 0, HIDE_ARTICLE: 1

                                                    
                                                    },
                                                     { DESCRIPTION: " the question description2", 
OPTIONS: ['option1', 'option2', 'option3', 'option4'], INSERTED_SENTENCE: "This is the sentence to be inserted.", TYPE: 2

                                                    
                                                    }
                                                    ]                                                    
                                                    }))

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
