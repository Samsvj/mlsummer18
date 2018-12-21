#!/usr/bin/python 

import smtplib
import getpass

#creating a connection to the gmail server

server=smtplib.SMTP("smtp.gmail.com:587")
server.starttls()

send=str(raw_input("enter the senders address:\t"))
passwd=str(getpass.getpass("enter the password:\t"))


server.login(send,passwd)
print "login done"

#now writing a message that will appear on the mail receiced by the receiver
rece=str(raw_input("enter the receivers address"))
message=str(raw_input("\nenter the message here"))

for i in range(0,2):
	server.sendmail(send,rece,message)
	print "send mail :)"

#closing the server
print"closing the server now"

server.quit()
