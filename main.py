import os
import webapp2
import urllib2

PATH = os.environ['PATH_INFO']
URL = 'https://<Your_region>-<Your_Project>.cloudfunctions.net' + PATH

class Handler(webapp2.RequestHandler):
  def get(self):
    response = urllib2.urlopen(URL)
    self.response.write(response.read())

app = webapp2.WSGIApplication([
  (PATH, Handler)
], debug=True)
