import nltk
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize

# sample_text = state_union.raw("2005-GWBush.txt")
sample_text = "pineapples on pizzas are delicious lol 420 blazeit"

words = word_tokenize(sample_text)
tagged = nltk.pos_tag(words)
print(tagged)

# tagged is a list of tuples with the word and its part of speech
# look up tag list online
