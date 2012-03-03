from google.appengine.ext import db
from google.appengine.ext.db import polymodel
from django.utils import simplejson as json
from models.utils import TEXT_DATA

def save_section(obj):
    section = Section()
    #for k in obj:
    #    section.__setattr__(k, obj[k])
    #section.__dict__ = obj
    section.from_obj(obj)
    section.put()
    return None # return error msg

def get_section(id):
    q = Section.all()
    q.filter('sectionid = ', id)
    return q.get()

class Section(polymodel.PolyModel):
    sectionid = db.StringProperty(indexed=True)
    sectiontype = db.StringProperty()

    def to_json_str(self):
        pass

