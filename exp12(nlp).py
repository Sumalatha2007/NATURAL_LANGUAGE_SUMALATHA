sentence = "the cat runs"

words = sentence.split()

grammar = {
"DET":["the","a"],
"NOUN":["cat","dog"],
"VERB":["runs","eats"]
}

if words[0] in grammar["DET"] and words[1] in grammar["NOUN"] and words[2] in grammar["VERB"]:
    print("Sentence accepted by grammar")
else:
    print("Sentence rejected")
