from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

TEMPLAGE_DIR = "templates/"
PAGE_DIR = TEMPLAGE_DIR + "pages/"

def render_page(handler, page_name, values):
    handler.response.out.write(template.render(PAGE_DIR + page_name, values))
