# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter url - ')
count = int(raw_input('Enter count - '))
position = int(raw_input('Enter position - '))

i = 0
print url

while i < count:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[position-1].get('href', None)
    print url
    i = i +1
