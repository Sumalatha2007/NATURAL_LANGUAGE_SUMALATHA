import nltk

# Download required resources (run once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Input sentence
text = "The dog is playing in the garden"

# Tokenization
tokens = nltk.word_tokenize(text)

# POS Tagging
pos_tags = nltk.pos_tag(tokens)

# Print result
print("POS Tags:")
print(pos_tags)
