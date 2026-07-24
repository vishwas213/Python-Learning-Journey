text = input("Enter your text: ")

count = 1

for i in range(len(text)):
    if i == len(text) - 1:
        print(text[i] + str(count), end="")
    elif text[i] == text[i + 1]:
        count += 1
    else:
        print(text[i] + str(count), end="")
        count = 1