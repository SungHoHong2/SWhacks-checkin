from modals.Attendant import Attendant
from views.SessionHandler import SessionHandler
import urllib2
import json
from google.appengine.ext import ndb


class AddRegisterDataHandler(SessionHandler):
    def get(self):
        user = self.session.get('Auth')
        if not user:
            self.redirect("/")

        ndb.delete_multi(Attendant.query().fetch(999999, keys_only=True))  # Clear datastore entities
        ndb.get_context().clear_cache()  # Clear memcache

        req = urllib2.urlopen('https://api.typeform.com/v1/form/tPmlbe?key=c023bc0bb7371530bd64e4fd052759b41a74b93b&completed=true')
        data = json.load(req)

        raw_data = data.get('responses')

        for people in raw_data:

            if people.get('answers').get('email_40994675') is None:
                _email = '';
            else:
                _email = people.get('answers').get('email_40994675');

            a = Attendant(
                firstName=people.get('answers').get('textfield_40994669'),
                lastName=people.get('answers').get('textfield_40994670'),
                gender=people.get('answers').get('list_40994679_choice'),
                email=_email,
                tShirtSize=people.get('answers').get('list_40994681_choice'),
                dietaryPreferences=people.get('answers').get('list_40994680_choice'),
                specialAccomodations=people.get('answers').get('textarea_40994692'),
            )
            a.put()

        self.redirect("/list")

