import urllib
import json

url = raw_input('Enter url - ')
print "url entered:", url

input = urllib.urlopen(url).read()

info = json.loads(input)

print json.dumps(info, indent=4)

total = 0

counts = info["comments"]

for item in counts:

    total = total + int(item['count'])
print total
