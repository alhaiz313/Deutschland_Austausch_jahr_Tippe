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


class Register(webapp.RequestHandler):

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


    self.response.out.write(''' <form action="/new" enctype="multipart/form-data" method="get">
                <label for="un">User_name</label>
                <div> <input type="text" name="cont" id="un" /></div>
                <label for="pw">Password</label>
                <div> <input type="text" name="pw" id="un" /></div>
              <div><input type="submit" value="Submit"></div>
</form></html>
''')

    

    self.response.out.write('''<font size="3"><a href="/" style="text-decoration:none"> go to the Home Page
    </a></font>''')
  
                            
application = webapp.WSGIApplication([('/register', Register)], debug=True)


def main():
  run_wsgi_app(application)


if __name__ == "__main__":
  main()
