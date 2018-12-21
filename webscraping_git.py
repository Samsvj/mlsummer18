import requests
import bs4 
from  bs4 import BeautifulSoup as bs

wiki="https://github.com/redashu?tab=repositories"
page1="https://github.com/redashu?page=2&tab=repositories"
page2="https://github.com/redashu?page=3&tab=repositories"



url = requests.get(wiki)
url1 = requests.get(page1)
url2= requests.get(page2)

soup = bs(url.content,"lxml")
soup1 = bs(url1.content,"lxml")
soup2 = bs(url2.content,"lxml")

links = soup.find_all("a")

for link in links:
	print "<a href='%s'>%s </a>" %(link.get("href"), link.text)
	
#g_data = soup.find_all("div", {"class":"li"})
n=67
i=0

for th in range (n):
	try:			
		print soup.find_all("h3")[th].text
		print "\t" + soup.find_all("relative-time")[th].text
	except:
		pass
for th in range (n):
	try:	
		print soup1.find_all("h3")[th].text
		print "\t" + soup1.find_all("relative-time")[th].text
	except:
		pass
for th in range (n):
	try:	
		print soup2.find_all("h3")[th].text
		print "\t" + soup2.find_all("relative-time")[th].text
	except:
		pass
	'''print th.contents[0].find_all("f6",{"class":"text-gray.mt-2"})[0].text	
	try:
		print th.contents[1].find_all("li",{"class":"primary"})[0].text
	except:
		pass'''

