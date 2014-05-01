import cgi
import datetime
import wsgiref.handlers
import os
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.api import images
from google.appengine.ext.webapp import template
from TipModel import *


class New(webapp.RequestHandler):

  def get(self):
    
    be = Benutzer()
    
    be.benutzer=self.request.get('cont')
    be.password=self.request.get('pw')
    if not be.benutzer or not be.password:
      self.redirect('/missing')
      return
    
    name=self.request.get('cont')
    q=db.Query(Benutzer)
    
    for tip in q:
      if name==tip.benutzer:
        self.redirect('/used')
        return
      else:
        pass
        

        
    """be.benutzer=self.request.get('cont')
    be.password=self.request.get('pw')
    if not be.benutzer or not be.password:
      self.redirect('/missing')
      return"""
    
    be.put()
    self.redirect('/first')
    









application = webapp.WSGIApplication([('/new', New)], debug=True)


def main():
  run_wsgi_app(application)


if __name__ == "__main__":
  main()
