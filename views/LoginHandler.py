from google.appengine.ext.webapp import template
import webapp2, os
from modals.User import getHash, User
from views.SessionHandler import SessionHandler


class LoginHandler(SessionHandler):
    # On get request, first check the user if logged in already. if not, render the login.html
    def get(self):
        user = self.session.get('Auth')
        if user:
            self.redirect("/list")

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
                query = User.all(keys_only=True)
                query.filter("email =", email)
                resultKey = query.get()

                self.session['Auth'] = "Yes"
                self.session['key'] = str(resultKey)
                self.session['Type'] = result.type
                self.redirect("/list")
            else:
                template_values = {
                    'css_url': "templates/css/style.css",
                    'status': "Invalid email or password",
                    'emailText': email
                }
                path = os.path.join(os.path.dirname(__file__), '../templates/login.html')
                self.response.out.write(template.render(path, template_values))
