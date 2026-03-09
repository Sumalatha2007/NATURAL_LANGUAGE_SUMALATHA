import random

sentence = "I play football"

words = sentence.split()

tags = ["NN","VB","JJ"]

for word in words:
    print(word,"->",random.choice(tags))
