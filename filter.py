from word import Word
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()
ps = PorterStemmer()
class Filter():

	def __init__(self):
		self.words = dict()


	def trim_word(self, word):
		# Helper method to trim away some of the non-alphabetic characters
		# I deliberately do not remove all non-alphabetic characters.
		word = word.strip(' .:,-!()"?+<>*')
		word = word.lower()
                word = word.decode("utf8")
                word = ps.stem(word)
                word = lmtzr.lemmatize(word)
		return word


	def train(self, train_file):
		lineNumber = 1
		ham_words = 0
		spam_words = 0
                stop = set(stopwords.words('english'))

		# Loop through all the lines
		for line in train_file:
			if lineNumber %2!= 0:
				line = line.split('\t')
				category = line[0]
				input_words = line[1].strip().split(' ')

				#Loop through all the words in the line, remove some characters
				for input_word in input_words:
					input_word = self.trim_word(input_word)
					if (input_word != "") and (input_word not in stop):

						# Check if word is in dicionary, else add
						if input_word in self.words:
							word = self.words[input_word]
						else:
							word = Word(input_word)
							self.words[input_word] = word

						# Check wether the word is in ham or spam sentence, increment counters
						if category == "ham":
							word.increment_ham()
							ham_words += 1
						elif category == "spam":
							word.increment_spam()
							spam_words += 1

						# Probably bad training file input...
						else:
							print "Not valid training file format"
                                                        #print input_word
						
		        lineNumber+=1

		# Compute the probability for each word in the training set
		for word in self.words:
			self.words[word].compute_probability(ham_words, spam_words)


	def get_interesting_words(self, sms):
		interesting_words = []
                stop = set(stopwords.words('english'))
		# Go through all words in the SMS and append to list. 
		# If we have not seen the word in training, assign probability of 0.4
		for input_word in sms.split(' '):
			input_word = self.trim_word(input_word)
			if (input_word != "") and (input_word not in stop):
				if input_word in self.words:
					word = self.words[input_word]
				else:
					word = Word(input_word)
					word.set_probability(0.40)
				interesting_words.append(word)

		# Sort the list of interesting words, return top 15 elements if list is longer than 15
		interesting_words.sort(key=lambda word: word.interesting(), reverse=True)
		return interesting_words[0:15]


	def filter(self, input_file, result_file):
		# Loop through all SMSes and compute total spam probability of the sms-message
		lineNumber = 0
		for sms in input_file:
			lineNumber+=1
			spam_product = 1.0
			ham_product = 1.0
			if lineNumber % 2 != 0:
				try:
					for word in self.get_interesting_words(sms):
						spam_product *= word.get_probability()
						ham_product *= (1.0 - word.get_probability())

					sms_spam_probability = spam_product / (spam_product + ham_product)
				except:
					result_file.write("error")
					
				if sms_spam_probability > 0.8:
					result_file.write("SPAM: "+sms)
				else:
					result_file.write("HAM: "+sms)
			result_file.write("\n")
