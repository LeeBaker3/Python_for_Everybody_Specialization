from BeautifulSoup import *
import urllib
url = raw_input("Enter - ")
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
total = 0

tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    value = tag.contents[0]
    total = total + int(tag.contents[0])

print total
