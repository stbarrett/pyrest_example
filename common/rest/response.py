""" Represents a response object """
import json


# noinspection PyInterpreter
class Response(Object):
    def __init__(self):
        self.data = None
        self.error = None
        self.error_code = None
        self.detailed_error_code = None
        pass

    def as_json(self):
        json_data = {}
        if self.data:
            json_data['data'] = self.data

        if self.error:
            json_data['error_code'] = self.error_code
            # only in debug mode, PROD should not see error message, only codes. Client responds appropriately.
            json_data['error'] = self.error
            json_data['detailed_error_code'] = self.detailed_error_code

        return json.dumps(json_data)
