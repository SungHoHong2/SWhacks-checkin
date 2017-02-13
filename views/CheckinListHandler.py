from google.appengine.ext.webapp import template
import os
from modals.Attendant import Attendant
import json
from views.SessionHandler import SessionHandler
from modals.MyJsonEncoder import MyJsonEncoder

col_names = {
    'firstName': 'firstName_lower',
    'lastName': 'lastName_lower',
    'email': 'email_lower'
}

class CheckinListHandler(SessionHandler):
    def get(self):
        user = self.session.get('Auth')
        if not user:
            self.redirect("/")

        '''
            1. make the pagination work based on the right google app engine protocal
            2. use the url paging data to track the page even if the page is refreshed
               ex) if you refresh your webpage on page 2, the refreshed data should remain in page 2

            3. search data - check
            4. total page check - check
            5. POST type change
            6. toggle update dummy add
                - simple check update
        '''



        prev_cursor = self.request.get('prev_cursor', '')
        next_cursor = self.request.get('next_cursor', '')
        attendant_list = Attendant.cursor_pagination(prev_cursor, next_cursor, 10)

        template_values = {
            'logout_url': '/logout',
            'changePass_url': '/chps',
            'attendant_list': json.dumps(attendant_list['objects'],cls=MyJsonEncoder),
            'next_cursor': attendant_list['next_cursor'],
            'prev_cursor' : attendant_list['prev_cursor'],
            'prev': attendant_list['prev'],
            'next': attendant_list['next'],
        }

        # Get user's type in session
        type = self.session.get('Type')
        if type == 'Administrator':
            template_values['addUser_url'] = '/adduser'
            template_values['type']= 'Admin' # Send Admin to html and render the add user button

        path = os.path.join(os.path.dirname(__file__), '../templates/checkin_list.html')
        self.response.out.write(template.render(path, template_values))


    def post(self):
        text = str(self.request.get('text'))
        col_name = col_names[str(self.request.get('col_name'))]

        attendant_list = Attendant.cursor_pagination('', '', Attendant.query().count(),
                         {'col_name': col_name, 'text': text.lower()})
        json_return = {
            'attendant_list': json.dumps(attendant_list['objects'],cls=MyJsonEncoder),
        }

        json_return = json.dumps(json_return)
        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        self.response.out.write(json_return)




