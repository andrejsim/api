
try:
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from pprint import pprint
import simplejson

# Yahoo! YQL API
PUBLIC_API_URL  = 'http://query.yahooapis.com/v1/public/yql'
OAUTH_API_URL   = 'http://query.yahooapis.com/v1/yql'
DATATABLES_URL  = 'store://datatables.org/alltableswithkeys'

class Query(object):

  def __init__(self):
    self.connection = HTTPConnection('query.yahooapis.com')

  def execute(self, yql, token = None):

    self.connection.request('GET', PUBLIC_API_URL + '?' + urlencode({ 'q': yql, 'format': 'json', 'env': DATATABLES_URL }))
    
    return simplejson.loads(self.connection.getresponse().read())

  def __del__(self):
    self.connection.close()


q = Query()

query = "select * from yahoo.finance.quotes where symbol in (\"AAPL\")"

pprint(q.execute(query))

query = "select * from yahoo.finance.quotes where symbol in (\"EURAUD=X\")"

pprint(q.execute(query))