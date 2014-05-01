from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from TipModel import *


class Delete(webapp.RequestHandler):

  def get(self):
    self.response.out.write('''<html> <style type="text/css">
<!--
	a:link {
	COLOR: #000;
	}
	a:visited {
	COLOR: #000;
	}
	a:hover {
	COLOR: #FF0000;
	}
	a:active {
	COLOR: #00FF00;
	}
	

body,td,th {
	font-size: 18px;
	color: #FFF;
}
.ygiy {
	font-family: Georgia, Times New Roman, Times, serif;
}
.ygiy {
	font-family: Tahoma, Geneva, sans-serif;
}
.soso {
	font-family: Trebuchet MS, Arial, Helvetica, sans-serif;
	color: #000;
}

-->
</style>

</head> 
<img src="/images/flagge-deutschland.gif" width="1200" height="100" />
<body bgcolor="#E78935"><blockquote><blockquote><h1>DEUTSCHLAND TIPS  (the life in Germany)</h1>
<blockquote><blockquote><img ALIGN="Right"src="/images/germany.gif" width="390" height="420" />
</blockquote></blockquote>
''')

    q = "SELECT * FROM Tip ORDER BY date DESC"	       
    tips = db.GqlQuery(q)

    user = users.get_current_user()
    i=-1
    self.response.out.write('''<form action="/v" enctype="multipart/form-data" method="get">''')
    
    
    for tip in tips:
      i=i+1
      self.response.out.write('''
                                <p><b>%s</b> wrote:</p>
<input type="checkbox" name="advice[%s]" value="%s" >%s<br>
<p><strong>__________________________________________________________</strong>
'''
                                % (tip.author.nickname(),i,tip.key(),tip.content))
        
    self.response.out.write('''</p><input type="submit" onclick="get_check_value()" value="remove">
</form>
''')


                                

  
                            
application = webapp.WSGIApplication([('/del', Delete)], debug=True)


def main():
  run_wsgi_app(application)


if __name__ == "__main__":
  main()
