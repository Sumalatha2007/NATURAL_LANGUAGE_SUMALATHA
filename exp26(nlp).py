# Simple English to French dictionary
dictionary = {
    "hello": "bonjour",
    "how": "comment",
    "are": "êtes",
    "you": "vous"
}

# input sentence
sentence = input("Enter English sentence: ")

# convert to lowercase and split words
words = sentence.lower().split()

# translate word by word
translated = []
for word in words:
    if word in dictionary:
        translated.append(dictionary[word])
    else:
        translated.append(word)

# join translated words
french_sentence = " ".join(translated)

# print output
print("French Translation:", french_sentence)
