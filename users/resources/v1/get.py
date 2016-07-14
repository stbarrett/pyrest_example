# handle android requests

import falcon
from common.exceptions.storage_error import StorageError
from common.models.users.users_collection import UsersCollection
from common.rest.response import Response as PyResponse


class Get(object):
    def on_get(self, request, response, uuid):
        py_response = PyResponse()
        try:
            users_collection = UsersCollection()
            user = users_collection.get(uuid)
            py_response.data = {'users': user.as_dict()}

            """ This should all go through a common dispatcher of some sort to handle errors in a single location """
        except StorageError as error:
            py_response.detailed_error_code = error.detailed_error_code
            py_response.error_code = error.error_code
            py_response.error = error.message

        response.body = py_response.as_json()
        response.status = falcon.HTTP_200  # For true REST, this should be a different code
