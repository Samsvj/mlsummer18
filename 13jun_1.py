#!/usr/bin/python

import tweepy
from textblob import TextBlob
#creating consumer key and secret key
#to authenticate twitter from ur account
consumer_key='KvrFMGd47vJabyo3eIT5e7dRH'

consumer_secret='r1TSviA2TLWWwnDcd8peqwwS1UNPDpkI0FhKSWdSAGC1wn63c3'

#creating access key and secret key

access_key='1007159846129451009-9iyLBDQPGOP472VJV7hZmITrtABLWv'
access_secret='aJWd8JnCxlhxXvFT4UXWAu1xokEA3WsCd3l1D8gfMLE5i'

#connecting for authentication
#here auth is very much similer to session variable

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_key,access_secret)

#connecting the API

connect=tweepy.API(auth)
#now we are connected
#now finding data
#print (dir(connect))
print ("HELLO THERE! \n")
searc=(str(raw_input("Enter about what you want to search today:\t")))
get_data=connect.search(searc,count=10)  #also define count like how many prints on this topic we need	
					#search('trump'.count=10) ---->>> no of tweets

#print(get_data)
#printing the data now

for i in get_data:
	print i.text
	analysis=TextBlob(i.text)
	print (analysis.sentiment)

