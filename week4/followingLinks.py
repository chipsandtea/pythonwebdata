import urllib.request
from bs4 import BeautifulSoup

url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter pos: '))
print('Retrieving: ' + url)
for i in range(count):
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html,'html5lib')
	tags = soup('a')
	j = 0
	for tag in tags:
		j+=1
		#print(tag.get('href',None))
		if j == pos:
			url = tag.get('href',None)
			print('Retrieving: ' + url)
			break