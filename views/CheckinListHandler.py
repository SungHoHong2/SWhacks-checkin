from google.appengine.ext.webapp import template
import webapp2, os
from google.appengine.api import users
from modals.Attendant import Attendant
from google.appengine.ext.db import Key
import json


class CheckinListHandler(webapp2.RequestHandler):
    def get(self):

        attendant_list = [{
            'id': attendant.put().id(),
            'first_name': attendant.firstName,
            'last_name': attendant.lastName,
            'email': attendant.email,
            'dietary_preferences': attendant.dietaryPreferences,
            'special_accomodations': attendant.specialAccomodations,
            'present': attendant.present
        } for attendant in Attendant.all()]


        template_values = {
            'logout_url': users.create_logout_url('/'),
            'attendant_list': json.dumps(attendant_list)
        }

        path = os.path.join(os.path.dirname(__file__), '../templates/checkin_list.html')
        self.response.out.write(template.render(path, template_values))
