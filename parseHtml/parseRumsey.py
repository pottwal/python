# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
url = "http://www.davidrumsey.com/luna/servlet/s/ug6vc9"
#htmlString = urllib2.urlopen(url).read()


#f = urllib2.urlopen(url)
#data = f.read()
#with open("rumseyDownload.html", "wb") as code:
#	code.write(data)


# html als String der open-Funktion zu übergeben
# geht nicht, da der String zu lang ist...
# deshalb wird erst heruntergeladen & gespeichert
# und dann diese html-Datei in BeautifulSoup geöffnet
soup = BeautifulSoup(open("rumseyDownload.html"))
liste =  soup.find_all('table')

print liste[4]

#for l in liste:
#	print l

#for link in soup.find_all('a'):
#    print(link.get('href'))

