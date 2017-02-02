import webapp2
from modals.Attendant import Attendant
from modals.User import User
from views.SessionHandler import SessionHandler

class TestDataHandler(SessionHandler):
    def get(self):
        a = Attendant(firstName='temp', lastName='', email='',
                    dietaryPreferences='', specialAccomodations='')
        a.generateTestData()


        u = User(email="t", password="d", type="Administrator")
        u.generateTestData()
        self.response.headers['Content_Type'] = 'text/plain'
        self.response.out.write('test successful.<br> Deleted old Attendees and Users.<br> Please readd them.')
