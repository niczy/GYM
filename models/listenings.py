from google.appengine.ext import db
from google.appengine.ext.db import polymodel
from django.utils import simplejson as json
from models.common import Section
from models.utils import TEXT_DATA

class ListeningSection(Section):
    audio = db.StringProperty()
    background = db.StringProperty()
    questions_json = db.TextProperty()


    def to_json_str(self):
        return json.dumps(self.to_obj())

    def to_obj(self):
        return {
            "sectionid": self.sectionid,
            "type": "listening",
            "audio": self.audio,
            "background": self.background,
            "questions": json.loads(self.questions_json)
        }

    @classmethod
    def from_dict(cls, dict_instance):
        listening_section = Section.get_by_sectionid(dict_instance.get('sectionid'))
        if listening_section:
            listening_section.audio = dict_instance.get('audio')
            listening_section.background = dict_instance.get('background')
            listening_section.questions_json = json.dumps(dict_instance.get('questions'))
            sectiontype = 'listening'
            return listening_section
        return ListeningSection(
                key_name = dict_instance.get('sectionid'),
                sectionid = dict_instance.get('sectionid'),
                audio = dict_instance.get('audio'), 
                background = dict_instance.get('background'),
                questions_json = json.dumps(dict_instance.get('questions')), 
                sectiontype = "listening")
        
if __name__ == '__main__':
    f = open('models/testdatas/listenings/listening-1.json')
    obj = json.loads(f.read())
    listening_section = ListeningSection.from_dict(obj)
    print listening_section.to_json_str()
    print listening_section.sectiontype


