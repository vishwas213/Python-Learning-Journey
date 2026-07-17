def count_frequency(text):
    counted = []

    for ch in text:
        if ch not in counted:
            count = 0

            for letter in text:
                if ch == letter:
                    count = count + 1

            print(ch, "->", count)
            counted.append(ch)


text = "banana"

count_frequency(text)