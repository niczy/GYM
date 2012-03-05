from google.appengine.ext import db
from google.appengine.ext.db import Model
from google.appengine.ext.db import polymodel
from django.utils import simplejson as json
import logging


class TestModel(db.Model):

    testid = db.StringProperty(indexed=True)
    readings = db.StringListProperty()
    listenings = db.StringListProperty()
    speakings = db.StringListProperty()
    writings = db.StringListProperty()

    def to_json_str(self):
        return json.dumps(self.to_dict())


    def to_dict(self):
        return {
            "testid": self.testid,
            "readings": self.readings,
            "writings": self.writings,
            "listenings": self.listenings,
            "writings": self.writings
        }

    @classmethod
    def get_by_testid(cls, testid):
        test_k = db.Key.from_path('TestModel', testid)
        return db.get(test_k)
        

    @classmethod
    def from_dict(cls, dict_instance):
        test = TestModel.get_by_testid(dict_instance.get('testid'))
        if test:
            test.readings = dict_instance.get('readings')
            test.listenings = dict_instance.get('listenings')
            test.speakings = dict_instance.get('speakings')
            test.writings = dict_instance.get('writings')
            return test

        return TestModel(
                key_name = dict_instance.get('testid'),
                testid=dict_instance.get('testid'),
                readings = dict_instance.get('readings'),
                listenings = dict_instance.get('listenings'),
                speakings = dict_instance.get('speakings'),
                writings = dict_instance.get('writings'))
        

if __name__ == "__main__":
    test_model = TestModel.from_dict({"id":"1", "speakings":["1", "2"], "writings":["1", "2"], "listenings":["1", "2"], "writings":["1", "2"], "readings": ["1", "2"]})
    print test_model.speakings
    print test_model.to_json_str()

