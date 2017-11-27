from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english")) # get english stopwords
# print(stop_words, len(stop_words))

dumb_sentence = "This iced tea is brewed from REAL tea leaves, never from power or concentrate. And it's sweetened with real sugar. So enjoy the pure and fresh taste of tea, straight ffrom the leaf to the bottle."
dumb_words = word_tokenize(dumb_sentence)

# filter out stop words from a sentence
filtered_words = []
for w in dumb_words:
    if not w in stop_words:
        filtered_words.append(w)
print(filtered_words) # doesn't include 'is' 'from' 'or' 'of' etc