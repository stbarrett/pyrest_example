# Small precise service that serves home page data for various clients

import falcon

from resources.android.index import Index as AndroidIndex
from resources.web.index import Index as WebIndex
from resources.xbox.index import Index as XboxIndex

# application is default for gunicorn
app = application = falcon.API()

# routes
app.add_route('/home/android', AndroidIndex())
app.add_route('/home/web', WebIndex())
app.add_route('/home/xbox', XboxIndex())
