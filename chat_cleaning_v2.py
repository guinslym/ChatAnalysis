import pandas as pd
import re
from itertools import chain

df = pd.read_csv('1516_1617ChatDataAnalysis.csv', encoding = "ISO-8859-1")

# print(df.head())

content = df['text']

# print(type(content))
print(content.size)


## Put QA rounds (cleaned records) in dictionay, with keys being record numbers
def makeDicts(content):
	d = {}
	for index in range(content.size):
		text = content[index]
		QAlist = extractQA(text, index)
		d[index] = QAlist
	return d


## extract each record, remove useless content, keep only the conversation, and order as a list in order that converstation occures
def extractQA(text, index):
	text = text.split("\r\r")
	# print(text)

	patternQt = "[0-9]{2}:[0-9]{2}[AP]M.*@twilio.libraryh3lp.com: (.*)"
	patternQw = "[0-9]{2}:[0-9]{2}[AP]M.*@web.libraryh3lp.com: (.*)"
	patternAn = "[0-9]{2}:[0-9]{2}[AP]M.*@chat.libraryh3lp.com: (.*)" 

	QAlist = []
	for i in range(len(text)):
		QA = re.findall(patternQt, text[i]) or re.findall(patternQw, text[i]) or re.findall(patternAn, text[i])

		if not any("offline message sent" in s for s in QA):
			QAlist.extend(QA)
	# print("lists:", QAlist)
	return QAlist


## get a list of all conversation records
def writeFile(d):

	with open("QAs.txt", "wb") as text_file:
		for key in d: 
			values = d[key]
			# print(values)
			line = (' '.join(values) + '\n\n')
			line = line.encode('utf-8')
			print(line)
			text_file.write(line)



# print records with give start and end record #
def printRecord(start, end):
	for i in range(start,end+1):
		record = d[i]
		print(record)




d = makeDicts(content)
print("lenght of d:", len(d))
printRecord(5,5)
writeFile(d)


