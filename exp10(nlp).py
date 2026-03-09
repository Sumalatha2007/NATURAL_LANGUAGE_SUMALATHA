sentence = ["I","play","games"]

tags = ["NN","NN","NN"]

for i in range(len(sentence)):
    if sentence[i] == "play":
        tags[i] = "VB"

for word,tag in zip(sentence,tags):
    print(word,"->",tag)
