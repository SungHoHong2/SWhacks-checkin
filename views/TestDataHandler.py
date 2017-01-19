import webapp2
from modals.Attendant import Attendant

class TestDataHandler(webapp2.RequestHandler):
    def get(self):
        a = Attendant(firstName='Steve', lastName='King', email='sking11@asu.edu',
                      dietaryPreferences='None', specialAccomodations='')
        a.put()
        a = Attendant(firstName='Ryan', lastName='Ang', email='rang1@asu.edu',
                      dietaryPreferences='Vegan', specialAccomodations='Pls no')
        a.put()
        a = Attendant(firstName='SungHo', lastName='Hong', email='sungho@asu.edu',
                      dietaryPreferences='None', specialAccomodations='')
        a.put()
        a = Attendant(firstName='Darrell', lastName='Jackson', email='bigdaddy@asu.edu',
                      dietaryPreferences='Pizza', specialAccomodations='Call me big daddy')
        a.put()
        self.response.headers['Content_Type'] = 'text/plain'
        self.response.out.write('test successful')
