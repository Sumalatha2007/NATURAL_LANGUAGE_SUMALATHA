import random

text = "I love natural language processing and I love python"

words = text.split()

bigrams = {}

for i in range(len(words)-1):
    key = words[i]
    value = words[i+1]
    if key not in bigrams:
        bigrams[key] = []
    bigrams[key].append(value)

word = random.choice(words)

result = [word]

for i in range(10):
    if word in bigrams:
        word = random.choice(bigrams[word])
        result.append(word)

print("Generated text:")
print(" ".join(result))
