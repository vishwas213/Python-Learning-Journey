# palindrome means same from both side
name = str(input("enter your word which you want to check"))

# check
if name[:] == name[::-1] :
    print(" this word is palindrome")
else:
    print("this word is not palindrome")
    