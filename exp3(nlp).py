from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("running", pos="v"))
print(lemmatizer.lemmatize("cars", pos="a"))
