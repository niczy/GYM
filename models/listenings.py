from google.appengine.ext import db
from google.appengine.ext.db import polymodel
from django.utils import simplejson as json
from models.common import Section
from models.utils import TEXT_DATA

def save_listening_section(obj):
    section = ListeningSection()
    #for k in obj:
    #    section.__setattr__(k, obj[k])
    #section.__dict__ = obj
    section.from_obj(obj)
    section.put()
    return None # return error msg

def get_listening_section(id):
    if id == None:
        return None;
    sections = db.GqlQuery("SELECT * FROM ListeningSection WHERE sectionid = :1", id)
    for section in sections:
        return section.to_obj()
    return None
    
class ListeningSection(Section):
    audio = db.StringProperty()
    background = db.StringProperty()
    questions_json = db.TextProperty()
    
    def to_json(self):
        return json.dumps(self.to_obj())

    def to_obj(self):
        return {
            "id": self.id,
            "type": self.sectiontype,
            "audio": self.audio,
            "background": self.background,
            "questions": json.loads(self.questions_json)
        }

    def from_obj(self, obj):
        self.id = obj['id']
        self.sectiontype = obj['type']
        self.audio = obj['audio'][TEXT_DATA]
        self.background = obj['background'][TEXT_DATA]
        self.questions_json = json.dumps(obj['question'])
        
