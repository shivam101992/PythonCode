import xml.etree.ElementTree as ET
import urllib

url = raw_input('Enter URL - ')
xml = urllib.urlopen(url).read()
sum1=0
tree=ET.fromstring(xml)

counts=tree.findall('comments/comment/count')

for count in counts:
	sum1+=int(count.text)
print sum1