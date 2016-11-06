import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter - ')
counter = int(input('Enter counter: '))
pos = int(input('Enter Position: '))
count = 0

while count<counter:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	# Retrieve all of the anchor tags
	tags = soup('a')
	url=tags[(pos-1)].get('href',None)
	count+=1

name=re.findall('known_by_([a-zA-Z]+).',url)	
for na in name:
	print na