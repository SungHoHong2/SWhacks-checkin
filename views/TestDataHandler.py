from modals.Attendant import Attendant
from modals.User import User
from views.SessionHandler import SessionHandler

class TestDataHandler(SessionHandler):
    def get(self):
        u = User(email="t", password="d", type="Administrator")
        u.generateTestData()
        self.redirect("/")