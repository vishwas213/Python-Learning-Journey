text = "aabbcddee"

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

print(frequency)