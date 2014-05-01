from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from TipModel import *



class Vanish(webapp.RequestHandler):
  def get(self):
    user =users.get_current_user()
    q = "SELECT * FROM Tip ORDER BY date DESC"
    tips = db.GqlQuery(q)
    i=-1
    for tip in tips:
      
      i=i+1
      n=i
      str(n)
      s= 'advice[%s]'% n
      v = self.request.get(s)
      if v:
        if tip.author == user or users.is_current_user_admin():
          tip.delete()
          #sself.redirect('/')
          
        else:
          self.redirect('/no')
          return
      """else:  
        self.redirect('/')"""
    self.redirect('/')
      

application = webapp.WSGIApplication([('/v', Vanish)], debug=True)


def main():
  run_wsgi_app(application)


if __name__ == "__main__":
  main()
