from google.appengine.ext.webapp import template
import webapp2, os
from google.appengine.api import users


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.redirect("/list")
        else:
            login_url = users.create_login_url('/')
            self.redirect(login_url)

