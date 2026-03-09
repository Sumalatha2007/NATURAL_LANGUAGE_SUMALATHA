from nltk.wsd import lesk
from nltk.corpus import wordnet

sentence = "I went to the bank to deposit money".split()

sense = lesk(sentence, "bank")

print("Word Sense:", sense)
print("Meaning:", sense.definition())
