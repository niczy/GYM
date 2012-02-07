from google.appengine.ext import db
from google.appengine.ext.db import polymodel
from django.utils import simplejson as json
from models.common import Section
from models.utils import TEXT_DATA

def save_reading_section(obj):
    section = ReadingSection()
    #for k in obj:
    #    section.__setattr__(k, obj[k])
    #section.__dict__ = obj
    section.from_obj(obj)
    section.put()
    return None # return error msg

def get_reading_section(id):
    if id == None:
        return None;
    sections = db.GqlQuery("SELECT * FROM ReadingSection WHERE sectionid = :1", id)
    for section in sections:
        return section.to_obj()
    return None

class ReadingSection(Section):
    article_json = db.TextProperty()
    questions_json = db.TextProperty()
 
    def to_json(self):
        return json.dumps(self.to_obj())

    def to_obj(self):
        return {
            "id": self.id,
            "type": self.sectiontype,
            "article": json.loads(self.article_json),
            "questions": json.loads(self.questions_json)
        }

    def from_obj(self, obj):
        self.id = obj['id']
        self.sectiontype = obj['type']
        self.article_json = json.dumps(obj['article'])
        self.questions_json = json.dumps(obj['question'])
        
