import cgi
import datetime
import wsgiref.handlers
import os
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.api import images
from google.appengine.ext.webapp import template
from TipModel import *


class MainPage(webapp.RequestHandler):
  
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
<script type="text/javascript">
<!--
function MM_swapImgRestore() { //v3.0
  var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
}
function MM_preloadImages() { //v3.0
  var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
    var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
    if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
}

function MM_findObj(n, d) { //v4.01
  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
    d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
  for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
  if(!x && d.getElementById) x=d.getElementById(n); return x;
}

function MM_swapImage() { //v3.0
  var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
   if ((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}
}

//-->
</script>

</head> 
<img src="/images/flagge-deutschland.gif" width="1250" height="100" />
<body bgcolor="#E78935"><blockquote><blockquote><h1>DEUTSCHLAND TIPS  (the life in Germany)</h1>
<blockquote><blockquote><img ALIGN="Right"src="/images/germany.gif" width="390" height="420" />
</blockquote></blockquote>
''')
    
    
    user = users.get_current_user()
   
    
    if user:
      
      
          
      q = "SELECT * FROM Tip ORDER BY date DESC"	
      tips = db.GqlQuery(q)
      for tip in tips:
        
        self.response.out.write('<p><b>%s</b> wrote:</p>' % tip.author.nickname())
        
          
          
        self.response.out.write('''<p class="soso"><img src='img?img_id=%s '></img>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<b>%s</b></div></p>''' %(
          tip.key(),cgi.escape(tip.content)))
      
        self.response.out.write('''<p><strong>__________________________________________________________</strong></p>''')        
      self.response.out.write("""
            <blockquote><form action="/sign" enctype="multipart/form-data" method="post">
              <label for="Deutschland tips">Write a Tip</label>
             
              <div><textarea name="content" rows="3" cols="60"></textarea></div>
              <div><input type="submit" value="Submit"></div>
              <p>                                  </p>
              <div><label>Put an Image:</label></div>
              <div><input type="file" name="img"/></div>
              
              
              </form></blockquote>
          </body>
        </html>""")
      
      self.response.out.write(
              '''<blockquote> Hello %s <br> Is administrator: %s
  <p></p><body onload="MM_preloadImages('/images/SignOut2.gif')">
  <a href="%s" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image7','','/images/SignOut2.gif',1)">
  <img src="images/SignOut1.gif" name="Image7" width="113" height="33" border="0" id="Image1" /></a>
  </body><body onload="MM_preloadImages('images/delete2.gif')">
<a href="del" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image4','','images/delete2.gif',1)">
<img src="images/delete1.gif" name="Image4" width="113" height="34" border="0" id="Image4" /></a>
</body>
              '''%(user.nickname(),users.is_current_user_admin(),users.create_logout_url("/")))
      
      if users.is_current_user_admin():
        self.response.out.write("""<body onload="MM_preloadImages('/images/Admin2.gif')">
  <a href="/_ah/admin" target="_blank" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image5','','/images/Admin2.gif',1)">
  <img src="images/Admin1.gif" name="Image5" width="113" height="33" border="0" id="Image1" /></a>
  </body></blockquote>""")

        
        
                                          
    else:
      self.redirect('/first')

class Deutschland(webapp.RequestHandler):
  def post(self):
    tip = Tip()
    if users.get_current_user():
      tip.author = users.get_current_user()
                            
    tip.content = self.request.get('content')
    avatar = self.request.get("img")
 
    if avatar:
      tip.avatar = db.Blob(avatar)
    else:
      pass
    tip.put()
    self.redirect('/')


"""class Check(webapp.RequestHandler):
  def get(self):
    self.redirect('/')
    
    user = users.get_current_user()
    L=[]
    i=-1
    b = "SELECT * FROM Benutzer ORDER BY date "
    c = db.GqlQuery(b)
    for a in c:
      #self.request.out.write('<h1> %s </h1>'% a.benutzer_name)
      L[i+1]=a.benutzer_name
    if user in L:
      self.redirect('/register') """

    


    
class Image (webapp.RequestHandler):
  def get(self):
	greeting = db.get(self.request.get("img_id"))
	if greeting.avatar:
	  self.response.headers['Content-Type'] = "image/png"
	  self.response.out.write(greeting.avatar)
	  
	else:
	  pass  

application = webapp.WSGIApplication([
  ('/', MainPage),
  #('/check', Check),
  ('/img', Image),
  ('/sign', Deutschland)
], debug=True)


def main():
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
