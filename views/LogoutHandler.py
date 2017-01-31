
from views.SessionHandler import SessionHandler


class LogoutHandler(SessionHandler):
    # On get request, delete the self.session
    def get(self):
        self.session.clear()
        self.redirect("/")
