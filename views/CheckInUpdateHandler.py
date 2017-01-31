from google.appengine.ext.webapp import template
import webapp2, os
from google.appengine.api import users
from modals.Attendant import Attendant
import json
from google.appengine.ext.db import Key

class CheckInUpdateHandler(webapp2.RequestHandler):
    def post(self):


        '''
            1. update the present column to True or False
            2. if update is successful then return the success value True
               and return the id of the updated object
            3. if update is unsuccessful then return the success value False
        '''

        is_present = self.request.get('is_present')
        _id = self.request.get('keys')

        print _id

        if is_present:
            print 'change present to false'
        else:
            print 'change present to true'


        response_data = {"success": True, 'keys': _id[0:len(_id)-1]}
        json_rtn = json.dumps(response_data)
        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        self.response.out.write(json_rtn)


