import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'dog' | 'cat'
VP -> 'runs' | 'eats'
""")

parser = nltk.ChartParser(grammar)

sentence = "dog runs".split()

for tree in parser.parse(sentence):
    print(tree)
