from modals.Attendant import Attendant
from views.SessionHandler import SessionHandler
import csv
import urllib2, json

class ExportCSVHandler(SessionHandler):
    def get(self):

        self.response.headers['Content-Type'] = 'application/csv'
        writer = csv.writer(self.response.out)

        req = urllib2.urlopen(
            'https://api.typeform.com/v1/form/tPmlbe?key=c023bc0bb7371530bd64e4fd052759b41a74b93b&completed=true')
        data = json.load(req)


        csv_dict = {}
        raw_data = data.get('responses')
        for people in raw_data:

            if people.get('answers').get('email_40994675') is not None:
                csv_dict[people.get('answers').get('email_40994675')] = people.get('answers').get('textfield_40994671')


        writer.writerow(["first_name","last_name","email","school"])
        for attendant in Attendant.query().filter(Attendant.present == True):
            writer.writerow([ attendant.firstName,
                              attendant.lastName,
                              attendant.email,
                              csv_dict[attendant.email] ])
