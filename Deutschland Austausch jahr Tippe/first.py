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



class First(webapp.RequestHandler):

  def get(self):
    self.response.out.write('''<html>


<style type="text/css">
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
<img src="/images/flagge-deutschland.gif" width="1250" height="100" />
<body bgcolor="#E78935"><blockquote><blockquote><h1>DEUTSCHLAND TIPS  (the life in Germany)</h1>
<blockquote><blockquote><img ALIGN="Right"src="/images/germany.gif" width="390" height="420" />
</blockquote></blockquote>
''')
    q = "SELECT * FROM Tip ORDER BY date DESC"	
    tips = db.GqlQuery(q)
    for tip in tips:
      
      self.response.out.write('<p><b>%s</b> wrote:</p>' % tip.author.nickname())
        
      self.response.out.write('''<p class="soso"><img src='img?img_id=%s '></img>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<b>%s</b></div></p>''' %(
      tip.key(),cgi.escape(tip.content)))
      
      self.response.out.write('''<p><strong>__________________________________________________________</strong></p>''')        

    
    self.response.out.write('''<font size="5">Hello Guest <a href="%s">Sign in</a> or
<a href="/register">Register</a></font>
'''% users.create_login_url('/check'))

                                
    """<script type="text/javascript">
alert("you are not a member, please register or sign in if you have an account")
</script>"""
  
                            
application = webapp.WSGIApplication([('/first', First)], debug=True)


def main():
  run_wsgi_app(application)


if __name__ == "__main__":
  main()
