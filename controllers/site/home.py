'''
Created on Dec 3, 2011

@author: charliezhang
'''
from controllers import render_page
from controllers import require_login
from controllers import RequestHandler
from controllers import JSONRequestHandler
from django.utils import simplejson as json

class HomePage(RequestHandler):
    @require_login('/landing')
    def get(self):
	    render_page(self, "home_page.html", None)


class TestMenu(JSONRequestHandler):
    @require_login(None)
    def get(self):
        #limit = self.request.get('limit');
        #order = self.request.get('order');
        '''
        testid: "1",
        title: "TPO 1",
        viewer: 1421,
        buyer: 12,
        uploader: "Zero",
        uploadTime: "2011-12-03",
        uploaderPortrait: "/asd/asd",
        rating: 3.8,
        price: 0,
        status: "done"
        '''
        
        self.response_json('{"items":['
                      '{"testid":"1","title":"Kaplan 1.0","viewer":1421,"buyer":12,"uploader":"KP","uploadTime":"2011-12-03","rating":3.8,"price":0,"status":"done","uploaderPortrait":"/static/images/portraits/ETS.png","lastUseTime":"2012-1-1"},'
                      '{"testid":"9","title":"Kaplan 3.0","viewer":132,"buyer":14,"uploader":"KP","uploadTime":"2011-12-03","rating":3.8,"price":103,"status":"done","uploaderPortrait":"/static/images/portraits/ETS.png","lastUseTime":"2012-1-1"},'
                      '{"testid":"2","title":"Kaplan 2","viewer":134,"buyer":56,"uploader":"KP","uploadTime":"2011-11-03","rating":4.0,"price":10,"status":"new","uploaderPortrait":"/static/images/portraits/ETS.png"}'
                      '],"itemnum":"16","description":"From Server"}')

class TestDetail(RequestHandler):
    @require_login(None)
    def get(self, testid):
        #TODO(nice) Get detail information for the test: #testid.
        # Such as Title, price, user's status of the test etc.
        render_page(self, "test_detail_page.html",
            {
             'testid': testid,
             'title': '=== TPO 2 ===',
             'description': 'TPO is the short name for Toefl Practice Online, the practice is made by ETS base on ,,'})
        
class TestHistoryList(JSONRequestHandler):
    def get(self):
        testid = int(self.request.get('testid'))
        pageid = int(self.request.get('pageid'))
        #TODO(nice): return a list of the user who had tried the test(testid), reverse time order
        if pageid == 1:
            self.response_json(json.dumps({
                "pagenum": 4,
                "items":[
                    {"user": "zx19890827",
                     "date": "2011-12-2"},
                    {"user": "nich01as",
                     "date": "2011-8-4"},
                    {"user": "drizzle",
                     "date": "2011-8-1"},
                    {"user": "Zero",
                     "date": "2010-9-15"}
                 ]}))
        else:
            self.response_json(json.dumps({
                "pagenum": 4,
                "items":[
                    {"user": "HAHAHA",
                     "date": "2009-12-2"},
                    {"user": "Whatshallido",
                     "date": "2009-8-4"},
                    {"user": "Ina",
                     "date": "2009-8-1"},
                    {"user": "Pan",
                     "date": "2008-9-15"}
                 ]}))
                          
    
