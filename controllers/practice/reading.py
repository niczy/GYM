from controllers.parameters import ARTICLE
from controllers.parameters import QUESTIONS
from controllers.parameters import OPTIONS
from controllers.parameters import DESCRIPTION
from controllers import render_page
from controllers import RequestHandler
from controllers import JSONRequestHandler
from controllers import require_login
import json

class ReadingPage(RequestHandler):
    @require_login('/landing')
    def get(self, testid, sectionid):
        render_page(self, "reading_page.html", {'testid': testid, "sectionid": sectionid})


class ApiGetReadingSection(JSONRequestHandler):

    def get(self):
        self.response_json(json.dumps({
                                        ARTICLE:['p1', 'p2', 'p3'], 
                                        QUESTIONS:[{
                                                DESCRIPTION: "This is the question description1", 
                                                OPTIONS: ['option1', 'option2', 'option3', 'option4']
                                                    
                                                    },
                                                    
                                                    { DESCRIPTION: "This is the question description2", 
                                                OPTIONS: ['option1', 'option2', 'option3', 'option4']
                                                    
                                                    }]
                                                    
                                                    }))
