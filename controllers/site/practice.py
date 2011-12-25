from controllers import render_page
from controllers import require_login
from controllers import RequestHandler
from controllers import JSONRequestHandler

class PracticeMenuPage(RequestHandler):
    @require_login('/landing')
    def get(self):
        render_page(self, 'practice_menu_page.html', None)
        
        
        
class PracticeMenu(JSONRequestHandler):
    @require_login(None)
    def get(self):
        #TODO(nice): return a list of practices of a specific type.
        # practice _type is reading/writing/listening/speaking
        practice_type = self.request.get('practice_type');
        
        if practice_type == 'reading':
            self.response_json('{"practiceitems":['
                      '{"practiceid":2,"title":"Barron Reading 1","viewer":1421,"uploader":"KP","uploadTime":"2011-12-03","rating":4.8,"status":"done"},'
                      '{"practiceid":4,"title":"Barron Reading 2","viewer":1542,"uploader":"KP","uploadTime":"2011-11-03","rating":4.0,"status":"new"},'
                      '{"practiceid":5,"title":"Barron Reading 3","viewer":134,"uploader":"KP","uploadTime":"2011-11-03","rating":3.0,"status":"new"}'

                      '],"name":"default","practicenum":"3","description":"From Server Practices."}')
       
        elif practice_type == 'listening':
             self.response_json('{"practiceitems":['
                      '{"practiceid":8,"title":"Barron Listening 1","viewer":1,"uploader":"ETS","uploadTime":"2011-12-03","rating":4.8,"status":"done"},'
                      '{"practiceid":9,"title":"Barron Listening 2","viewer":99999,"uploader":"Zero","uploadTime":"2011-11-03","rating":4.0,"status":"new"},'
                      '{"practiceid":10,"title":"Barron Listening 3","viewer":9,"uploader":"Nic","uploadTime":"2011-11-03","rating":3.0,"status":"new"}'

                      '],"name":"default","practicenum":"3","description":"From Server Practices."}')
       
        else:
            return
