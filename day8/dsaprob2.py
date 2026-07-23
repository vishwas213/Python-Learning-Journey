text = input("Enter your text: ")

words = text.split()

largest = ""

for word in words:
    if len(word) > len(largest):
        largest = word

print("Longest word =", largest)