from google.appengine.ext.webapp import template
from google.appengine.ext import db

import webapp2, os
from google.appengine.api import users
from modals.User import getHash, User


class LoginHandler(webapp2.RequestHandler):
    # On get request, first check the user if logged in already. if not, render the login.html
    def get(self):
        user = users.get_current_user()
        if user:
            self.redirect("/list")
        else:
            template_values = {
                'css_url': "templates/css/style.css"
            }
            path = os.path.join(os.path.dirname(__file__), '../templates/login.html')
            self.response.out.write(template.render(path, template_values))

    # On POST request, query the database for correct password
    def post(self):
        email = self.request.POST.get("email")
        password = self.request.POST.get("password")
        hashed = getHash(password)
        query = User.all()
        query.filter("email =", email)

        result = query.get()
        if result is None:
            template_values = {
                'css_url': "templates/css/style.css",
                'status': "Invalid email or password",
                'emailText': email
            }
            path = os.path.join(os.path.dirname(__file__), '../templates/login.html')
            self.response.out.write(template.render(path, template_values))
        else:
            if result.password == hashed:  # If same password, go to list page
                self.redirect("/list")
            else:
                template_values = {
                    'css_url': "templates/css/style.css",
                    'status': "Invalid email or password",
                    'emailText': email
                }
                path = os.path.join(os.path.dirname(__file__), '../templates/login.html')
                self.response.out.write(template.render(path, template_values))
