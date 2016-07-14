# handle android requests

import falcon
import json
from common.models.users.users_collection import UsersCollection
from common.rest.response import Response as PyResponse


class Index(object):
    def on_get(self, request, response):
        users_collection = UsersCollection()
        users = users_collection.find_all()

        results = []
        for user in users:
            results.append(user.as_dict())

        py_response = PyResponse()
        py_response.data = {'users': results}

        response.body = py_response.as_json()
        response.status = falcon.HTTP_200
