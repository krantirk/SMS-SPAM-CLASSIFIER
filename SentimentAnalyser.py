from word import Word
from nltk.tokenize import word_tokenize
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
import nltk.classify.util
sentiment_dictionary = {}
neg = []
neg.append("No")
neg.append("not")
neg.append("Never")
neg.append("None")
neg.append("Noone")
neg.append("hadnt")
neg.append("cant")
neg.append("Nope")
neg.append("shouldnt")
neg.append("havent")
class Filter1():

	def __init__(self):
		self.words = dict()
	def word_feats(words):
    		return dict([(word, True) for word in words])

	def train(self, train_file):

		# Loop through all the lines
		for line in train_file:
			if 1!= 0:
				word, score = line.split('\t')
                                sentiment_dictionary[word] = int(score)
	


	def filter(self, input_file, result_file):
		# Loop through all SMSes and compute total spam probability of the sms-message
		lineNumber = 0
		for sms in input_file:
                        words = word_tokenize(sms.lower())
                        negctr = 0
                        for word in words:
				word = word.lower()
                        	if word in neg:
                                	negctr += 1
			lineNumber+=1
			res=0
			if lineNumber % 2 != 0:
				try:
					res = sum( sentiment_dictionary.get(word, 0) for word in words )
                                        if negctr % 2 != 0:
                                        	res *= -1 
				except:
					result_file.write("error")
					
				if res > 2:
					result_file.write("POSITIVE "+sms)
				elif res < -2:
					result_file.write("NEGATIVE "+sms)
					#print res
                                else:
                                        result_file.write("NEUTRAL "+sms)
			result_file.write("\n")
