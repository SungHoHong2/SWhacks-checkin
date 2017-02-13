import json
from datetime import datetime


# http://stackoverflow.com/a/29185081
# internal class to handle datetime object
class MyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            # format however you like/need
            return obj.strftime("%Y-%m-%d %H:%M:%S.%f")
        # pass any other unknown types to the base class handler, probably
        # to raise a TypeError.
        return json.JSONEncoder.default(self, obj)