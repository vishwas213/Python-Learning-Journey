text = input("enter your text : ")

removed = ""

for ch in text:
    if ch not in removed:
        removed = removed + ch

print(removed)