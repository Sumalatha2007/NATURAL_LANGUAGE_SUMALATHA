from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["running","playing"]

for word in words:
    print(word,"->",ps.stem(word))
