from controllers import JSONRequestHandler

class ApiStoreAnswer(JSONRequestHandler):
    
    def post(self, testid, sectionid, questionid):

        self.response_json({"testid": testid, "sectionid": sectionid, "questionid": questionid})

    def get(self, testid, sectionid, questionid):
        return self.post(testid, sectionid, questionid)

    
