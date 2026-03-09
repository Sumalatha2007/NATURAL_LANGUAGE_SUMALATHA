from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
"cat likes milk",
"dog likes bone",
"cat and dog are pets"
]

vectorizer = TfidfVectorizer()

tfidf = vectorizer.fit_transform(docs)

print(tfidf.toarray())
