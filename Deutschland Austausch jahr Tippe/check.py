from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from TipModel import *



class Check(webapp.RequestHandler):

  
  def get(self):
     
    
    user = users.get_current_user()

    
      
  
    """q = "SELECT * FROM Tip ORDER BY date "	
    tips = db.GqlQuery(q)"""
    q=db.Query(Benutzer)
   
    for tip in q:
      if not user:
        self.redirect('/')
        return

      if tip.benutzer == user.nickname():
        
        self.redirect('/')
        return

    #self.redirect('/first')
    self.redirect('/joke')
      
  
      

        
    
      
    
      
application = webapp.WSGIApplication([('/check', Check)], debug=True)


def main():
  run_wsgi_app(application)


if __name__ == "__main__":
  main()

