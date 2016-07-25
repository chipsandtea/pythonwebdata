import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter URL: ')
print('Retrieving: ' + url)
xml = urllib.request.urlopen(url).read()
print('Retrieved ' + str(len(xml)) + ' characters')
tree = ET.fromstring(xml)

# XPath Selector
counts = tree.findall('.//count')
print('Count: ' + str(len(counts)))

sum = 0
for item in counts:
	sum += int(item.text)

print('Sum: ' + str(sum))