from google.appengine.ext import db
from google.appengine.ext.db import polymodel
from django.utils import simplejson as json
from models.common import Section
from models.utils import TEXT_DATA

class ReadingSection(Section):
    article = db.TextProperty()
    questions = db.TextProperty()

    def to_json_str(self):
        return json.dumps(self.to_obj())

    def to_obj(self):
        return {
            "sectionid": self.sectionid,
            "type": "reading",
            "article":  json.loads(self.article),
            "questions": json.loads(self.questions)
        }

    @classmethod
    def from_dict(cls, dict_instance):
        reading_section = Section.get_by_sectionid(dict_instance.get("sectionid")) 
        if reading_section:
            reading_section.artilce = json.dumps(dict_instance.get('article'))
            reading_section.questions = json.dumps(dict_instance.get('article'))
            reading_section.sectiontype = 'reading'
            return reading_section
        return ReadingSection(
                key_name = dict_instance.get('sectionid'),
                sectionid =dict_instance.get('sectionid'),
                article                 = json.dumps(dict_instance.get('article')),
                questions               = json.dumps(dict_instance.get('questions')),
                sectiontype = 'reading')


if __name__ == '__main__':
    f = open('models/testdatas/readings/reading-1.json')
    obj = json.loads(f.read())
    reading_section = ReadingSection.from_dict(obj)
    print reading_section.to_json_str()
    print reading_section.sectiontype


