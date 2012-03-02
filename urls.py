from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from views import MainPage
from settings import DEBUG

application = webapp.WSGIApplication([
        # main page
        ('/', MainPage),
    ], debug = DEBUG)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
