# -*- coding: utf-8 -*-

#import xml.etree.ElementTree as ET
#namespaces = {'kml': 'http://earth.google.com/kml/2.2'}
#tree = ET.parse('irt.kml')
#root = tree.getroot()

#for place in root.iter('kml:Placemark'):
	# hier interessieren nur Punkte, keine Flächen
	# => Placemarks ohne Attribut id ignorieren

#	if place.attrib:
#		print place.attrib



from xml.etree.ElementTree import ElementTree
tree = ElementTree()
root = tree.parse("irt.kml")
print root
for place in root.iter('kml:Placemark'):
	# hier interessieren nur Punkte, keine Flächen
	# => Placemarks ohne Attribut id ignorieren

	if place.attrib:
		print place.attrib




