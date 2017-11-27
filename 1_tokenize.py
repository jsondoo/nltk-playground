from nltk.tokenize import sent_tokenize, word_tokenize

# tokenizing - word tokenizer, sentence tokenizer
# lexicon and corpora
# corpora - body of text ex: speeches, journals, English language
# lexicon - vocabulary of a person, language, or branch of knowledge
## different people use different words with context

# NLTK is a powerful that can tokenize for us
english_text = "Mr. Andrews, natural language processing with python is easy. The sky is blue."
print(sent_tokenize(english_text))
print(word_tokenize(english_text))

for i in word_tokenize(english_text):
    print(i) # Notice that punctuation counts as a word by default

