from google.appengine.ext.webapp import template
import webapp2, os
from google.appengine.api import users
from modals.Attendant import Attendant
from google.appengine.ext import ndb
import json


class CheckInUpdateHandler(webapp2.RequestHandler):
    def post(self):

        '''
            1. update the present column to True or False
            2. if update is successful then return the success value True
               and return the id of the updated object
            3. if update is unsuccessful then return the success value False
        '''

        # extract self.request.get("keys") into an array and loop through all of them
        # 1. for each item, get the key
        # 2. Take key and get attendant from it
        # 3. invert the attendant's present boolean
        # 4. put into database
        # 5. make a copy of the key, and place into an array called "_id"




        # This works for one user.
        key_str = self.request.get("keys").split(',')[0]

        key = ndb.Key(urlsafe=key_str)
        attendant = key.get()

        is_present = attendant.present
        # If the attendant is present, mark him/her not present
        # We do this inversion because a staff member might have checked the wrong person
        if is_present:
            attendant.present = False
        else:
            attendant.present = True

        attendant.put()

        _id = self.request.get("keys").split(',')[0]
        # this works for one user

        if is_present:
            print 'change present to false'
        else:
            print 'change present to true'

        response_data = {"success": True, 'id': _id}
        json_rtn = json.dumps(response_data)
        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        self.response.out.write(json_rtn)
