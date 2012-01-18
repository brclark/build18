#!/usr/bin/python

from urllib import urlretrieve
import imp
urlretrieve('https://raw.github.com/gist/1194123/fbconsole.py', '.fbconsole.py')
fb = imp.load_source('fb', '.fbconsole.py')

fb.AUTH_SCOPE = ['publish_stream']
fb.authenticate()

status = fb.graph_post("/me/feed", {"message": "Hello from python"})
