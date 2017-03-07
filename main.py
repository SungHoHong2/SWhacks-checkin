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
from views.LogoutHandler import LogoutHandler
from views.ChangePasswordHandler import ChangePasswordHandler
from views.AddUserHandler import AddUserHandler
from views.AddRegisterDataHandler import AddRegisterDataHandler

config = {}
config['webapp2_extras.sessions'] = {
    'session_max_age' : 43200, # 12 hours of session
    'secret_key': 'sTm9uZXIWCxIJQXR0ZW5kYW50GICAgICA4JcJDA',
}
app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/logout', LogoutHandler),
    ('/chps', ChangePasswordHandler),
    ('/adduser', AddUserHandler),
    ('/list', CheckinListHandler),
    ('/update', CheckInUpdateHandler),
    ('/synchronize_user', TestDataHandler),
    ('/synchronize_data', AddRegisterDataHandler),
], debug=True, config=config)
