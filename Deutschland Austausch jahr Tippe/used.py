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



class Used(webapp.RequestHandler):
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
    
    self.response.out.write(''' <font size="5"><p>Sorry this user name is already used</p>''')
    self.response.out.write('''<font size="3"><a href="/register" style="text-decoration:none"> go to the signing up page
    </a></font><br>''')
    self.response.out.write('''<font size="3"><a href="/first" style="text-decoration:none"> go to the Home Page
    </a></font>''')
    #self.response.out.write('''<h1> hello </h1>''')
      
    
application = webapp.WSGIApplication([('/used', Used)], debug=True)


def main():
  run_wsgi_app(application)


if __name__ == "__main__":
  main()
