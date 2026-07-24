# Find the first repeated character.

text = input("Enter your text: ")

repeat = "" 

for ch in text:
    if ch in repeat:
        print("first repeated word is : ",ch)
        # break
    else:
        repeat = repeat + ch
