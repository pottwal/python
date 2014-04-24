# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import re
tree = ET.parse('irt.kml')
root = tree.getroot()
namespaces = {'kml': 'http://earth.google.com/kml/2.2'}

# there is no namespace parameter for the iterator -
# => code kml namespace hard
for place in root.iter('{http://earth.google.com/kml/2.2}Placemark'):
	# of interest here are only points, not areas
	# => ignore Placemarks without attribute id
	if place.attrib:
		print place.find('kml:name',namespaces=namespaces).text.encode('utf-8')
		#coord = place.find('kml:Point/kml:coordinates',namespaces=namespaces).text
		#print "long,lat (kml): " + coord.encode('utf-8')
		# description ist CDATA ist => über regex IRT-Nummern herausziehen
		description = place.find('kml:description',namespaces=namespaces).text
		coord = re.findall(r"<h5>Coordinates: (.*)</h5>",description)
		for c in coord:
			print "Koordinaten lat,long: " + c
		# get types of placemark, may help in identifying toponyms
		# haha
		type = re.findall(r"<h4>(.*)</h4>",description)
		for t in type:
			print t.encode('utf-8')
		listIrt = re.findall(r"/(IRT\d\d\d)\.html", description)
		for l in listIrt:
			print l.encode('utf-8')


