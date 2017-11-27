# stemming - form of data pre-processing where we remove affixes from a word
# ex: reader -> read, reading -> read
# possible to use a lot of important information if not careful

from nltk.stem import PorterStemmer
ps = PorterStemmer()

words = ["catchy", "catching", "catch", "caught", "octopus", "octopuses", "octopi", "desks", "desk"]
for w in words:
    print(ps.stem(w))

