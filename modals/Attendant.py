from google.appengine.ext import ndb
from google.appengine.datastore.datastore_query import Cursor


class Attendant(ndb.Model):
    firstName = ndb.StringProperty('FirstName')
    lastName = ndb.StringProperty('LastName')
    email = ndb.StringProperty('Email')

    '''
        Using lowercase is also impossible in Google App Engine
    '''
    firstName_lower = ndb.ComputedProperty(lambda self: self.firstName.lower())
    lastName_lower = ndb.ComputedProperty(lambda self: self.lastName.lower())
    email_lower = ndb.ComputedProperty(lambda self: self.email.lower())

    dietaryPreferences = ndb.StringProperty('DietaryPreferences')
    specialAccomodations = ndb.StringProperty('SpecialAccomodations')
    present = ndb.BooleanProperty('Present', default=True)
    created = ndb.DateTimeProperty(auto_now_add=True)

    def generateTestData(self):
        a = Attendant(firstName='Steve', lastName='King', email='sking11@asu.edu',
                      dietaryPreferences='None', specialAccomodations='')
        a.put()
        a = Attendant(firstName='Ryan', lastName='Ang', email='rang1@asu.edu',
                      dietaryPreferences='Vegan', specialAccomodations='Pls no')
        a.put()
        a = Attendant(firstName='SungHo', lastName='Hong', email='sungho@asu.edu',
                      dietaryPreferences='None', specialAccomodations='')
        a.put()
        a = Attendant(firstName='Darrell', lastName='Jackson', email='bigdaddy@asu.edu',
                      dietaryPreferences='Pizza', specialAccomodations='Call me big daddy')
        a.put()

    @classmethod
    def cursor_pagination(cls, prev_cursor_str, next_cursor_str, total_page, search_dict=False):


        '''
            Currently it is impossible for me to create paging while searching
            Because the Google App Engine uses cursors and ordering the rows are important for paging
            While when we use operands for searching -> ordering is prohibited
        '''

        if search_dict:
            limit = search_dict['text'][:-1] + chr(ord(search_dict['text'][-1]) + 1)
            for property, value in vars(cls).iteritems():
                if search_dict['col_name'] is property:
                    col_name = value
            query_start = cls.query(col_name >= search_dict['text'].lower(), col_name < limit)

            # query_start = cls.query(ndb.OR(cls.firstName_lower >= search_dict['text'].lower(), cls.lastName_lower >= search_dict['text'].lower(),
            #                                   cls.email_lower >= search_dict['text'].lower()))
        else:
            if prev_cursor_str:
                query_start = cls.query().order(-cls.created)
            else:
                query_start = cls.query().order(cls.created)


        if not prev_cursor_str and not next_cursor_str:
            objects, next_cursor, more = query_start.fetch_page(total_page)
            prev_cursor_str = ''
            if next_cursor:
                next_cursor_str = next_cursor.urlsafe()
            else:
                next_cursor_str = ''
            next_ = True if more else False
            prev = False
        elif next_cursor_str:
            cursor = Cursor(urlsafe=next_cursor_str)
            objects, next_cursor, more = query_start.fetch_page(total_page, start_cursor=cursor)
            prev_cursor_str = next_cursor_str
            next_cursor_str = next_cursor.urlsafe()
            prev = True
            next_ = True if more else False
        elif prev_cursor_str:
            cursor = Cursor(urlsafe=prev_cursor_str)
            objects, next_cursor, more = query_start.fetch_page(total_page, start_cursor=cursor)
            objects.reverse()
            next_cursor_str = prev_cursor_str
            prev_cursor_str = next_cursor.urlsafe()
            prev = True if more else False
            next_ = True

        objects = [{
            'id': attendant.put().urlsafe(),
            'first_name': attendant.firstName,
            'last_name': attendant.lastName,
            'email': attendant.email,
            'dietary_preferences': attendant.dietaryPreferences,
            'special_accomodations': attendant.specialAccomodations,
            'present': attendant.present
        } for attendant in objects]

        return {'objects': objects, 'next_cursor': next_cursor_str, 'prev_cursor': prev_cursor_str, 'prev': prev, 'next': next_}


