from google.appengine.ext import db
from google.appengine.ext.db import polymodel
from django.utils import simplejson as json
from models.common import Section
from models.utils import TEXT_DATA

class WritingSection(Section):
    description = db.TextProperty()
    passage = db.TextProperty()
    lecture = db.StringProperty()
 
    def to_json_str(self):
        return json.dumps(self.to_obj())

    def to_obj(self):
        return {
            "sectionid": self.sectionid,
            "type": "reading",
            "description":  self.description,
            "lecture": self.lecture,
            "passage": self.passage
        }

    @classmethod
    def from_dict(cls, dict_instance):
        return WritingSection(sectionid =dict_instance.get('sectionid'),
                description = dict_instance.get('description'),
                passage = dict_instance.get('passage'),
                lecture = dict_instance.get('lecture'))


if __name__ == '__main__':
    f = open('models/testdatas/writings/writing-1.json')
    obj = json.loads(f.read())
    writing_section = WritingSection.from_dict(obj)
    print writing_section.to_json_str()


