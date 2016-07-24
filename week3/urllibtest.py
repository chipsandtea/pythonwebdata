import urllib.request

fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')

'''for line in fhand:
	print(line.strip().decode('utf-8'))'''

counts = dict()
for line in fhand:
	words = line.decode('utf-8').split()
	for word in words:
		counts[word] = counts.get(word,0) + 1
print(counts)