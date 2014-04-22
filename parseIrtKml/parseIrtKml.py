# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import re
tree = ET.parse('irt.kml')
root = tree.getroot()
namespaces = {'kml': 'http://earth.google.com/kml/2.2'}

# beim Iterator scheints keinen namespace Parameter zu geben -
# also Namespace hart codieren
for place in root.iter('{http://earth.google.com/kml/2.2}Placemark'):
	# hier interessieren nur Punkte, keine Flächen
	# => Placemarks ohne Attribut id ignorieren
	if place.attrib:
		print "\n" # + place.get('id')
		print place.find('kml:name',namespaces=namespaces).text.encode('utf-8')
		#coord = place.find('kml:Point/kml:coordinates',namespaces=namespaces).text
		#print "long,lat (kml): " + coord.encode('utf-8')
		# description ist CDATA ist => über regex IRT-Nummern herausziehen
		description = place.find('kml:description',namespaces=namespaces).text
		coord = re.findall(r"<h5>Coordinates: (.*)</h5>",description)
		for c in coord:
			print "Koordinaten lat,long: " + c
		# typ ausgeben
		type = re.findall(r"<h4>(.*)</h4>",description)
		for t in type:
			print t.encode('utf-8')
		listIrt = re.findall(r"/(IRT\d\d\d)\.html", description)
		for l in listIrt:
			print l.encode('utf-8')


