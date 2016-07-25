import urllib.request
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html5lib')

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup('span')
sum = 0
for tag in tags:
	sum += int(tag.contents[0])
print(sum)