from google.appengine.ext.webapp import template
import webapp2, os
from google.appengine.api import users


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.redirect("/checkin")
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)
            self.response.write(
                '<html><body>{}</body></html>'.format(greeting))


        #
        # path = os.path.join(os.path.dirname(__file__), '../templates/index.html')
        # self.response.out.write(template.render(path, {}))
        #
        #
