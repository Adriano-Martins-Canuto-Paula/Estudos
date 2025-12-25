import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sample_text = "I am Phillosopher in Portgual's city"
tokens = word_tokenize(sample_text)

#Unigram
unigram = list(ngrams(tokens, 1))
print('Unigrams:', unigram)

#Bigram
bigram = list(ngrams(tokens, 2))
print("Bigrams:", bigram)

#Trigrams
trigram = list(ngrams(tokens, 3))
print('Trigrams:', trigram)


#desafio fazer o mesmo agora com letras e nao com palavras