import sys
import string
import re
import logging
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models

qa_file = "QAs.txt"
sw_file = 'sw_customized.txt'


def model(filename, num_topics, num_words, passes):
	
	# creat a logging file
	logging.basicConfig(filename='lda_model.log', format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

	texts = process_text(filename)
	## Constructing a document-term matrix
	# The Dictionary() function traverses texts, assigning a unique integer id to each unique token while also collecting word counts and relevant statistics. To see each token’s unique integer id, try print(dictionary.token2id).
	dictionary = corpora.Dictionary(texts)
	# print(dictionary.token2id)

	# doc2bow() function converts dictionary into a bag-of-word
	corpus = [dictionary.doc2bow(text) for text in texts]

	# print(corpus[0])

	# generate an LDA model
	ldamodel = models.ldamodel.LdaModel(corpus = corpus, num_topics = num_topics, id2word = dictionary, passes = passes)
	# ldamodel = models.ldamodel.LdaModel(corpus, num_topics)


	# review topics 
	print(ldamodel.print_topics(num_topics, num_words))

	return ldamodel



def process_text(filename):

	with open(filename, "r+", encoding = "utf-8") as f:
		lines = f.read().strip().split("\n\n")
		# print(len(lines))

	stopwrods = getSW()
	texts = []
	# each line is a Q or A, treated as a doc 
	# l = 0
	for line in lines: 
		line = line.strip().lower()
		# l+=1
		# print(l)
		# print(line)
	
		# re.findall('\s+', line)
		line = remove_punct(line)
		tokens = tokenize(line)

		# tokenization
		# tokenizer = RegexpTokenizer(r'\w+')
		# tokens = tokenizer.tokenize(line)

		# remove stop words from tokens
		stopped_tokens = [t for t in tokens if not t in stopwrods]

		# Create p_stemmer of class PorterStemmer and creat stemmed tokens 
		p_stemmer = PorterStemmer()
		stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

		texts.append(stemmed_tokens)

		# print(line)
		# print(tokens)
		# print(stopped_tokens)
		# print(stemmed_tokens)
	return texts




def getSW():
	# open file containing customized stopwords
	with open(sw_file, "r+") as swfile: 
		sw_lines = swfile.readlines()
	
	new_stop = sw_lines[0].lower().strip()
	new_stop = new_stop.split(', ')

	# print(new_stop)

	# get English stop words list for the package 
	en_stop = get_stop_words('en')

	# add new customized stopwrods 
	new_stop.extend(en_stop)

	# remove duplicate 
	new_stop = list(set(new_stop))
	# print(new_stop)
	return new_stop


# two helper functions for tokenziation 
def remove_punct(text):
    text_nopunct = ''.join([char for char in text if char not in string.punctuation])
    return text_nopunct

# print(string.punctuation)
def tokenize(text):
    tokens = re.split('\s+', text)
    return tokens

	


# process_text(qa_file)

if __name__ == '__main__':
	
	log = open("output.log", "a")
	sys.stdout = log

	passes = 20
	num_words = 7
	start = 2
	end = 20
	for t in range(start, end+1): 
		print("numer of topics:", t)
		model(qa_file, t, num_words, passes)





