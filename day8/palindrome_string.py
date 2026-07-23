text = input("enter any word : ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if reverse == text:
    print("text is Palindrome ")
else:
    print("text is not Palindrome ")