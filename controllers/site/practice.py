from controllers import render_page
from controllers import require_login
from controllers import RequestHandler
from controllers import JSONRequestHandler

class PracticeMenuPage(RequestHandler):
    @require_login('/landing')
    def get(self, *args):
        type = '';
        if len(args) == 0:
            type = 'reading'
        else:
            type = args[0]
        
        render_page(self, 'practice_menu_page.html', {'practice_type': type})
        
        
        
class PracticeMenu(JSONRequestHandler):
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
        practice_type = self.request.get('practice_type');
        if practice_type == 'reading':
            self.response_json('{"practiceitems":['
                      '{"practiceid":"2","title":"Barron Reading 1","viewer":1421,"uploader":"KP","uploadTime":"2011-12-03","rating":4.8,"status":"done"},'
                      '{"practiceid":"4","title":"Barron Reading 2","viewer":1542,"uploader":"KP","uploadTime":"2011-11-03","rating":4.0,"status":"new"},'
                      '{"practiceid":"5","title":"Barron Reading 3","viewer":134,"uploader":"KP","uploadTime":"2011-11-03","rating":3.0,"status":"new"}'

                      '],"name":"default","practicenum":"3","description":"From Server Practices."}')
        else:
            return
