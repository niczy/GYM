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
            "type": "writing",
            "description":  self.description,
            "lecture": self.lecture,
            "passage": self.passage
        }

    @classmethod
    def from_dict(cls, dict_instance):
        writing_section = Section.get_by_sectionid(dict_instance.get('sectionid'))
        if writing_section:
            writing_section.description = dict_instance.get('description')
            writing_section.passage = dict_instance.get('passage')
            writing_section.lecture = dict_instance.get('lecture')
            writing_section.sectiontype = 'writing'
            return writing_section
        return WritingSection(
                key_name = dict_instance.get('sectionid'),
                sectionid =dict_instance.get('sectionid'),
                description = dict_instance.get('description'),
                passage = dict_instance.get('passage'),
                lecture = dict_instance.get('lecture'),
                sectiontype = 'writing')


if __name__ == '__main__':
    f = open('models/testdatas/writings/writing-1.json')
    obj = json.loads(f.read())
    writing_section = WritingSection.from_dict(obj)
    print writing_section.to_json_str()


