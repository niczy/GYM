from google.appengine.ext import db
from google.appengine.ext.db import polymodel
from django.utils import simplejson as json

def save_section(obj):
    section = Section()
    #for k in obj:
    #    section.__setattr__(k, obj[k])
    #section.__dict__ = obj
    section.from_obj(obj)
    section.put()
    return None # return error msg

def get_section(id):
    if id == None:
        return None;
    sections = db.GqlQuery("SELECT * FROM Section WHERE sectionid = :1", id)
    for section in sections:
        return section.__dict__
        return section.to_obj()
    return None
    
class Section(polymodel.PolyModel):
    id = db.StringProperty(indexed=True)
    sectiontype = db.StringProperty()

    def to_json(self):
        return json.dumps(self.to_obj())
    
    def to_obj(self):
        return {
            "id": self.sectionid,
            "type": self.sectiontype
        }
    
    def from_obj(self, obj):
        self.id = obj['id']
        self.sectiontype = obj['type']

