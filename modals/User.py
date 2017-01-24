from google.appengine.ext import db
import hashlib


class User(db.Model):
    email = db.StringProperty('Email')
    password = db.StringProperty('Password')
    type = db.StringProperty('Type')

    def generateTestData(self):
        salt="swh4cks"
        tempPs = "123"
        passWord = getHash(tempPs)
        u = User(email='rang1@asu.edu', password=passWord, type="Administrator")
        u.put()

        tempPs = "password"
        passWord = getHash(tempPs)
        u = User(email='sungho@asu.edu', password=passWord, type="Administrator")
        u.put()

        tempPs = "hello"
        passWord = getHash(tempPs)
        u = User(email='bigdaddy@asu.edu', password=passWord, type="Staff")
        u.put()

def getHash(strToHash):
    salt = "swh4cks"
    return hashlib.md5(strToHash+salt).hexdigest()
