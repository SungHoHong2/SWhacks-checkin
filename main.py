# django oriented framework
# author : sunghohong
# ===================================
# modal : modals
# templates : front-end source files
# views : controllers
# ===================================

import webapp2
from views.MainHandler import MainHandler
from views.TestDataHandler import TestDataHandler
from views.LoginHandler import LoginHandler

app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/checkin', MainHandler),
    ('/test', TestDataHandler),
], debug=True)
