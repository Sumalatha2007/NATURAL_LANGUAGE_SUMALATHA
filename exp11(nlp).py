grammar = {
"S": ["NP VP"],
"NP": ["dog","cat"],
"VP": ["runs","eats"]
}

sentence = "dog runs"

words = sentence.split()

if words[0] in grammar["NP"] and words[1] in grammar["VP"]:
    print("Sentence is valid")
else:
    print("Invalid sentence")
