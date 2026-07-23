text = input("enter your text : ")

lenght = len(text)

a = text.count("a")
e = text.count("e")
i = text.count("i")
o = text.count("o")
u = text.count("u")

vowels = a + e + i + o + u

Consonants = lenght - vowels

print("vowels : ",vowels)
print("consonent : ",Consonants)