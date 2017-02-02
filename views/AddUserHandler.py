from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.ext.db import Key

import webapp2, os
from google.appengine.api import users
from modals.User import getHash, User
from views.SessionHandler import SessionHandler


class AddUserHandler(SessionHandler):
    # On get request, first check the user if logged in already. if not, render the login.html
    def get(self):
        user = self.session.get('Auth')
        if not user:
            self.redirect("/")

        template_values = {
            'css_url': "templates/css/style.css"
        }
        path = os.path.join(os.path.dirname(__file__), '../templates/add_user.html')
        self.response.out.write(template.render(path, template_values))

    # On POST request, query the database for correct password
    def post(self):
        email = self.request.POST.get("email")

        query = User.all()
        query.filter("email =", email)

        result = query.get()
        if result:
            template_values = {
                'css_url': "templates/css/style.css",
                'status': "That email is taken",
                'emailText': email
            }
            path = os.path.join(os.path.dirname(__file__), '../templates/add_user.html')
            self.response.out.write(template.render(path, template_values))
        else:
            password = self.request.POST.get("password")
            hashed = getHash(password)
            type = self.request.POST.get("typelist")
            if type != "Administrator":  # default to Staff if not administrator
                type = "Staff"
            user = User(email=email, password=hashed, type=type)

            user.put()
            self.redirect("/list")
