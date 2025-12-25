import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

sample_text = 'I like programation in JAVA and SQL'
tokens = word_tokenize(sample_text)

print('Tokens:', tokens)