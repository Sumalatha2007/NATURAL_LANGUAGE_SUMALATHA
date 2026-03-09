sentence = input("Enter sentence: ")

if "?" in sentence:
    print("Dialog Act: Question")
elif "please" in sentence:
    print("Dialog Act: Request")
else:
    print("Dialog Act: Statement")
