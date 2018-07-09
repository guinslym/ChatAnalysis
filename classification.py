import pandas as pd

doc_file = "train.txt"
label_file = "index_of_themes.csv"

with open(doc_file, "r+", encoding = "utf-8") as f: 
	docs = f.read().strip().split('\n\n')
	docs = pd.DataFrame(docs)
	print(len(docs))

with open(label_file, "r+", encoding = "utf-8") as csv_f:
	labels = pd.read_csv(csv_f, usecols = [1], header = None)
	print(len(labels))

assert(len(docs) == len(labels))

