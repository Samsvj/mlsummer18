#!/usr/bin/python 

import smtplib
#putting username and password here
username="pushpenders196"
password="Airport@123"

fromaddress="pushpenders196@gmail.com"
toaddress="pushpendersofficial@gmail.com"

#now writing a message that will appear on the mail receiced by the receiver

message=''' hello there how you doing '''

#creating a connection to the gmail server

server=smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(username,password)

for i in range(0,2):
	server.sendmail(fromaddress,toaddress,message)
	print "send mail :)"

#closing the server
print"closing the server now"

server.quit()
