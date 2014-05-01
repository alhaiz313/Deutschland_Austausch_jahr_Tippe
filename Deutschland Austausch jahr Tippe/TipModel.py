
from google.appengine.ext import db


class Tip(db.Model):
  author = db.UserProperty()
  content = db.StringProperty(multiline=True)
  avatar = db.BlobProperty()
  date = db.DateTimeProperty(auto_now_add=True)


class Benutzer(db.Model):
  benutzer=db.StringProperty()
  password=db.StringProperty()
  
