import urllib
import json

url=raw_input('Enter URL - ')
ur=urllib.urlopen(url)
data=ur.read()
js=json.loads(data)
sum1=0
for comment in js['comments']:
	sum1+=comment['count']

print sum1	