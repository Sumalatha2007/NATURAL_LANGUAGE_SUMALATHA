import nltk

sentence = "The small cat chased the mouse"

tokens = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(tokens)

grammar = "NP: {<DT>?<JJ>*<NN>}"

cp = nltk.RegexpParser(grammar)

tree = cp.parse(tags)

print(tree)
