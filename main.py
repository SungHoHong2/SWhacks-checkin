# django oriented framework
# author : sunghohong
# ===================================
# modal : modals
# templates : front-end source files
# views : controllers
# ===================================

import webapp2
from views.CheckinListHandler import CheckinListHandler
from views.CheckInUpdateHandler import CheckInUpdateHandler
from views.TestDataHandler import TestDataHandler
from views.LoginHandler import LoginHandler

app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/list', CheckinListHandler),
    ('/update', CheckInUpdateHandler),
    ('/test', TestDataHandler),
], debug=True)
