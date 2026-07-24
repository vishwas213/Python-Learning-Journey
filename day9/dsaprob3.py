# Check if two strings are anagrams.
text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

if sorted(text1) == sorted(text2):
    print("Anagram")
else:
    print("Not Anagram")