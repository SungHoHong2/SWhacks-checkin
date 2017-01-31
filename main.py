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
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'sTm9uZXIWCxIJQXR0ZW5kYW50GICAgICA4JcJDA',
}
app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/logout', LogoutHandler),
    ('/list', CheckinListHandler),
    ('/update', CheckInUpdateHandler),
    ('/test', TestDataHandler),
], debug=True, config=config)
