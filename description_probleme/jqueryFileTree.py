#
# jQuery File Tree
# Python/Django connector script
# By Martin Skou
#
import os
import urllib
from django.http.response import HttpResponse
from Proto1.settings import BASE_DIR

def dirlist(request):
   r=['<ul class="jqueryFileTree" style="display: none;">']
   try:
       r=['<ul class="jqueryFileTree" style="display: none;">']
       d=urllib.parse.unquote(BASE_DIR+"/Workspace/"+request.GET.get('dir','c:\\temp'))
       for f in os.listdir(d):
           ff=os.path.join(d,f)
           my_path = ff.replace(BASE_DIR+"/Workspace/", "")
           if os.path.isdir(ff):
               r.append('<li class="directory collapsed"><a href="#" rel="%s/">%s</a></li>' % (my_path,f))
           else:
               e=os.path.splitext(f)[1][1:] # get .ext and remove dot
               r.append('<li class="file ext_%s"><a href="#" rel="%s">%s</a></li>' % (e,my_path,f))
       r.append('</ul>')
   except Exception as e:
       r.append('Could not load directory: %s' % str(e))
   r.append('</ul>')
   return HttpResponse(''.join(r))