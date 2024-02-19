# Import necessary modules from NLTK
import nltk
import numpy as np


from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# Download the necessary NLTK data (only needed once)
nltk.download('punkt')
nltk.download('stopwords')

# Sample text to be tokenized
text = "Hello there! How are you today? This is an example of sentence tokenization."

# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentence Tokenization:")
print(sentences)

# Word Tokenization
words = word_tokenize(text)
print("\nWord Tokenization:")
print(words)

stopWords = set(stopwords.words('english'))

filteredList = []

for word in words:
    if word.casefold() not in stopWords:
        filteredList.append(word)

print("\nFiltered Tokenization:")
print(filteredList)
