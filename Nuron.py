from nltk.tokenize import word_tokenize
import numpy as np 
import nltk
from  nltk.stem.porter import PorterStemmer


Stemmer =  PorterStemmer()


def tokenize(sentence):
    return  nltk.word_tokenize(sentence)

def stem(word):
    return Stemmer.stem(word.lower())

def bag_word(tokenized_sentence,words):
    sentence_words = [stem(word)for word in tokenized_sentence]
    bag = np.zeros(len(words),dtype=np.float32)
    for idx , w in enumerate(words):
     if w in sentence_words :
         bag[idx] =  1 

         return bag 

 
   

