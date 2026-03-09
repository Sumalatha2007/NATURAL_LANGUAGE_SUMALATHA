def ends_with_ab(s):
    if len(s) >= 2 and s[-2:] == "ab":
        return True
    return False

string = input("Enter string: ")

if ends_with_ab(string):
    print("Accepted: String ends with 'ab'")
else:
    print("Rejected")
