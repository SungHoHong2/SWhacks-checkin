from modals.Attendant import Attendant
from views.SessionHandler import SessionHandler
import csv

class ExportCSVHandler(SessionHandler):
    def get(self):

        self.response.headers['Content-Type'] = 'application/csv'
        writer = csv.writer(self.response.out)
        writer.writerow(["first_name\tlast_name\temail"])

        for attendant in Attendant.query().filter(Attendant.present == True):
            writer.writerow([attendant.firstName, attendant.lastName, attendant.email])

            #print "{0}\t{1}\t{2}\n".format(attendant.firstName, attendant.lastName, attendant.email)
            #output_aray.append("{0}\t{1}\t{2}\n".format(attendant.firstName, attendant.lastName, attendant.email))




