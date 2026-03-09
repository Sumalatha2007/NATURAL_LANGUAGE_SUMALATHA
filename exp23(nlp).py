text = "The cat sits on the mat. The dog runs in the park."

sentences = text.split(".")

if len(sentences) > 1:
    print("Text is coherent")
else:
    print("Text lacks coherence")
