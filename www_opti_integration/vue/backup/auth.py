'''
Created on 5 juin 2014

@author: georges
'''


#! /usr/bin/python

from cgi import parse_qs
from wsgiref.simple_server import make_server
 
def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    if environ['REQUEST_METHOD'] == 'POST':
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        request_body = environ['wsgi.input'].read(request_body_size)
        d = parse_qs(request_body) # turns the qs to a dict
        return 'From POST: %s' % ''.join('%s: %s' % (k, v) for k, v in d.iteritems())
    else: # GET
        d = parse_qs(environ['QUERY_STRING']) # turns the qs to a dict
        return 'From GET: %s' % ''.join('%s: %s' % (k, v) for k, v in d.iteritems())
 
    httpd = make_server('', 1337, simple_app)
    print ("Serving on port 1337...")
    httpd.serve_forever()