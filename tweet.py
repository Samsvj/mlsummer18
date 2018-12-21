#!/usr/bin/python         

import tweepy
from textblob import TextBlob
import matplotlib as plot

#creating consumer key and secret key
#to authenticate twitter from ur account
consumer_key='KvrFMGd47vJabyo3eIT5e7dRH'

consumer_secret='r1TSviA2TLWWwnDcd8peqwwS1UNPDpkI0FhKSWdSAGC1wn63c3'

#creating access key and secret key

access_key='1007159846129451009-9iyLBDQPGOP472VJV7hZmITrtABLWv'
access_secret='aJWd8JnCxlhxXvFT4UXWAu1xokEA3WsCd3l1D8gfMLE5i'

#connecting for authentication

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)

#connecting to API

connect=tweepy.API(auth)

#now we are connected
#finding the data

#print dir(connect)

get_data=connect.search("islam")

for i in get_data:
	print i.text
	analyser=TextBlob(i.text)
	print(analyser.sentiment)
