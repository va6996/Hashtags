try:
    import json
    import jsonpickle
    import sys
    import os
    import json
    import csv
    import tweepy
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import datetime
import time

CONSUMER_KEY = '2D2O7p2WcSflcIwPUFkpO8H4d'
CONSUMER_SECRET = 'McQbicLfcY7O6MAh1BTX0T3GybBlA3kx2ypBF3VsQ0uNlIkAcn'
ACCESS_TOKEN = '706688188236955648-13KhxQqozsjU1SLsgbYspIQ1SPFfcsp'
ACCESS_SECRET = 'hewOf2eUI6DugndlGLiJRNp3KdE4i19yoakRUOWf9D815'

count=0
while True:
	oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
	twitter_stream = TwitterStream(auth=oauth)
	iterator =  twitter_stream.statuses.sample(language='en') 
	   
	now = datetime.datetime.now().strftime("%Y-%m-%d")
	now+='.txt'

	for tweet in iterator:
		if 'text' in tweet:
			if "RT" not in tweet['text']:
				with open(now,'a') as f:
					f.write(json.dumps(tweet)+'\n')
					count+=1
	print count
	time.sleep(5)    

