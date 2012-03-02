from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from models import Status
from datetime import datetime, timedelta
import os
from settings import SITE_TITLE

# main view class
class MainPage(webapp.RequestHandler):
    def get(self):
        # get all the statuses
        query = Status.all()

        # pass all the statuses and the sitetitle to the template
        template_values = {
            'sitetitle': SITE_TITLE,
            'statuses': query,
        }

        # find the template
        path = os.path.join(os.path.dirname(__file__), 'index.html')

        # render the template
        self.response.out.write(template.render(path, template_values))
