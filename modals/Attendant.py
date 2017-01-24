from google.appengine.ext import db


class Attendant(db.Model):
    firstName = db.StringProperty('FirstName')
    lastName = db.StringProperty('LastName')
    email = db.StringProperty('Email')
    dietaryPreferences = db.StringProperty('DietaryPreferences')
    specialAccomodations = db.StringProperty('SpecialAccomodations')
    present = db.BooleanProperty('Present', default=False)

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