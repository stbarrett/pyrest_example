# Small precise service that serves home page data for various clients

import sys

paths = ['/vagrant/pyrest']
for p in paths:
    sys.path.insert(0, p)

import falcon
from resources.v1.index import Index as V1Index
from resources.v1.get import Get as V1Get

# application is default for gunicorn
app = application = falcon.API()

# routes
app.add_route('/users/1', V1Index())
app.add_route('/users/1/{uuid}', V1Get())
