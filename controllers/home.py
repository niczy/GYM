'''
Created on Dec 3, 2011

@author: charliezhang
'''
from controllers import render_page
from controllers import require_login
from controllers import RequestHandler
from controllers import JSONRequestHandler

class HomePage(RequestHandler):
    @require_login(None)
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
        
        self.Response('{"testitems":['
                      '{"testid":"1","title":"Kaplan 1.0","viewer":1421,"buyer":12,"uploader":"KP","uploadTime":"2011-12-03","rating":3.8,"price":0,"status":"done","uploaderPortrait":"/static/images/portraits/ETS.png"},'
                      '{"testid":"2","title":"Kaplan 2","viewer":134,"buyer":56,"uploader":"KP","uploadTime":"2011-11-03","rating":4.0,"price":10,"status":"new","uploaderPortrait":"/static/images/portraits/ETS.png"}'
                      '],"name":"default","testnum":"16","description":"From Server"}')
