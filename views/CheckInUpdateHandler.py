import webapp2
from google.appengine.ext import ndb

import json
from modals.MyJsonEncoder import MyJsonEncoder
from datetime import datetime


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
        # key_str = self.request.get("keys").split(',')[0]

        #print 'howdy'
        key_list = self.request.get("keys").split(',')
        key_list = key_list[:len(key_list) - 1:]
        mod_list = self.request.get("modified").split(',')
        mod_list = mod_list[:len(mod_list) - 1:]
        prese_list = self.request.get("present").split(',')
        prese_list = prese_list[:len(prese_list) - 1:]
        #print key_list
        for i,key_str in enumerate(key_list):
            #print 'gohowdy'
            #print key_str
            key = ndb.Key(urlsafe=key_str)
            attendant = key.get()

            dataBaseModified = attendant.modified
            GUIModifiedStr = mod_list[i]
            GUIModifiedDate = datetime.strptime(GUIModifiedStr,"%Y-%m-%d %H:%M:%S.%f")
            if dataBaseModified <= GUIModifiedDate:
                # Case 1: the database and GUI is the same, update both sides
                # Case 2: the database is outdated, GUI is the same, update both sides
                is_present = attendant.present
                # If the attendant is present, mark him/her not present
                # We do this inversion because a staff member might have checked the wrong person
                if is_present:
                    attendant.present = False
                    prese_list[i] = False  # Tell present is updated
                else:
                    attendant.present = True
                    prese_list[i] = True  # Tell present is updated

                attendant.modified = datetime.now()  # update time
                mod_list[i] = attendant.modified.strftime("%Y-%m-%d %H:%M:%S.%f")  # Tell GUI time is updated
                attendant.put()
                print "DEBUG. updated database and GUI", attendant.firstName
            else:
                # Case 3: Database is newer than GUI, so update just GUI by moving values from db to GUI
                prese_list[i] = attendant.present
                mod_list[i] = dataBaseModified.strftime("%Y-%m-%d %H:%M:%S.%f")
                print "DEBUG. updated GUI", attendant.firstName

        response_data = {"success": True, 'keys': key_list, 'modified': mod_list, 'present': prese_list}
        json_rtn = json.dumps(response_data, cls=MyJsonEncoder)
        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        self.response.out.write(json_rtn)
