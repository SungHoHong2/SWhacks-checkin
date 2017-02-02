from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.ext.db import Key

import webapp2, os
from google.appengine.api import users
from modals.User import getHash, User
from views.SessionHandler import SessionHandler


class ChangePasswordHandler(SessionHandler):
    # On get request, first check the user if logged in already. if not, render the login.html
    def get(self):
        user = self.session.get('Auth')
        if not user:
            self.redirect("/")

        template_values = {
            'css_url': "templates/css/style.css"
        }
        path = os.path.join(os.path.dirname(__file__), '../templates/change_pass.html')
        self.response.out.write(template.render(path, template_values))

    # On POST request, query the database for correct password
    def post(self):
        password = self.request.POST.get("password")
        hashed = getHash(password)
        key = self.session.get('key')
        key_obj = Key(key)
        user = db.get(key_obj)

        user.password = hashed
        user.put()
        self.redirect("/list")


