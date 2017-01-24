import webapp2
from modals.Attendant import Attendant
from modals.User import User

class TestDataHandler(webapp2.RequestHandler):
    def get(self):
        a = Attendant(firstName='temp', lastName='', email='',
                    dietaryPreferences='', specialAccomodations='')
        a.generateTestData()
        u = User(email="t", password="d", type="Administrator")
        u.generateTestData()
        self.response.headers['Content_Type'] = 'text/plain'
        self.response.out.write('test successful')
