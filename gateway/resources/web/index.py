# handle android requests

from util import handleBasicResponse


class Index(object):
    def on_get(self, request, response):
        handleBasicResponse('web', response)
