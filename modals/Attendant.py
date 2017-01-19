from google.appengine.ext import ndb

class Attendant(ndb.Model):
    firstName = ndb.StringProperty('FirstName')
    lastName = ndb.StringProperty('LastName')
    email = ndb.StringProperty('Email')
    dietaryPreferences = ndb.StringProperty('DietaryPreferences')
    specialAccomodations = ndb.StringProperty('SpecialAccomodations')
    present = ndb.BooleanProperty('Present', default=False)

def generateTestData():
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