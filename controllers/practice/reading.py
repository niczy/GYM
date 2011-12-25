from controllers.parameters import ARTICLE
from controllers.parameters import QUESTIONS
from controllers.parameters import OPTIONS
from controllers.parameters import DESCRIPTION
from controllers.parameters import OPTION_NUMBER
from controllers.parameters import TYPE
from controllers.parameters import INSERTED_SENTENCE
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
                                        ARTICLE:["Googe is a <gym reference-id='0' type='highlight'>sexual</gym> act originating in the Amazon <gym reference-id='2'></gym>rainforest. It is where the man wraps <gym reference-id='2'></gym>his legs around a womans face and googe's like a bad badger. It is now used as an exclamation of hornyness or used as a term instead of fuck, or also c", 'formerly known as Google, the new name Googe was implemented on the 14th of February 2007 (Valentines day) with a chocolate covered strawberry kicking ou', "Originated as a typo on the Google homepage, on Feb 14 of 2007 its was supposed to be a special <gym reference-id='1'>valentines day</gym> Google loge, but the artist misspelled Google. "], 
                                        QUESTIONS:[{
                                                DESCRIPTION: "This is the question description1", 
                                                OPTIONS: ['this is an option', 'option2', 'option3', 'option4'], TYPE: 0
                                                    
                                                    },
                                                    
                                                    { DESCRIPTION: " the question description2", 
OPTIONS: ['option1', 'option2', 'option3', 'option4'], OPTION_NUMBER: 2, TYPE: 0

                                                    
                                                    },
                                                     { DESCRIPTION: " the question description2", 
OPTIONS: ['option1', 'option2', 'option3', 'option4'], INSERTED_SENTENCE: "This is the sentence to be inserted.", TYPE: 2

                                                    
                                                    }
                                                    ]                                                    
                                                    }))
