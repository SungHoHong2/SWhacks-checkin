from google.appengine.ext.webapp import template
import webapp2, os
from google.appengine.api import users

class MainHandler(webapp2.RequestHandler):
    def get(self):

        print users.create_logout_url('/')

        template_values = {
            'logout_url': users.create_logout_url('/')
        }

        path = os.path.join(os.path.dirname(__file__), '../templates/index.html')
        self.response.out.write(template.render(path, template_values))
