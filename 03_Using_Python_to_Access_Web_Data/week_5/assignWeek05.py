# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter url - ')

print url

xmldoc = urllib.urlopen(url).read()
tree = ET.fromstring(xmldoc)
counts = tree.findall('.//count')
total = 0
for item in counts:
    total = total + int(item.text)
print total
