
from google.appengine.ext import db
from google.appengine.ext.db import polymodel
from django.utils import simplejson as json
from models.common import Section
from models.utils import TEXT_DATA

class SpeakingSection(Section):

    description = db.TextProperty()
    narrator_audio = db.StringProperty()
    paragraph = db.TextProperty()
    audio = db.StringProperty()
    background = db.StringProperty()
 
    def to_json_str(self):
        return json.dumps(self.to_obj())

    def to_obj(self):
        return {
            "sectionid": self.sectionid,
            "type": "reading",
            "description": self.description, 
            "narrator_audio": self.narrator_audio,
            "paragraph": self.paragraph,
            "audio": self.audio,
            "background": self.background
        }

    @classmethod
    def from_dict(cls, dict_instance):
        return SpeakingSection(sectionid =dict_instance.get('sectionid'),
                description = dict_instance.get('description'),
                narrator_audio = dict_instance.get('narrator_audio'),
                paragraph = dict_instance.get('paragraph'),
                audio = dict_instance.get('audio'),
                background = dict_instance.get('background'))


if __name__ == '__main__':
    f = open('models/testdatas/speakings/speaking-1.json')
    obj = json.loads(f.read())
    speaking_section = SpeakingSection.from_dict(obj)
    print speaking_section.to_json_str()

