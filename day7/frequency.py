text ={
    "name" : "apple",
    "a" : 0,
    "p" : 0,
    "l" : 0,
    "e" : 0,
}

for ch in text["name"]:
    text[ch] = text[ch] +1


print("a : ", text["a"])
print("p : ", text["p"])
print("l : ", text["l"])
print("e : ", text["e"])

# i hai wi har baar badhega aur use badhe hue i ko vaule bana di jayegi ur diconary k