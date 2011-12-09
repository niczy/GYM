
from src.controllers.base.handlers import RequestHandler

class ListeningPage(RequestHandler):
    def get(self):        
        self.RenderPage();
