
import falcon

## helper functions
def handleBasicResponse(endpointStr, response):
  response.body = '{"endpoint": "%s"}' % endpointStr
  response.status = falcon.HTTP_200
  return response
