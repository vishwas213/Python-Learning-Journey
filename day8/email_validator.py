# Accept email only if:

# Contains @
# Contains .
# No spaces
email = input("enter yourr email : ")

count = email.count(" ")
dot = email.count(".")
add = email.count("@")

if count == 0 and dot == 1 and add == 1:
    print("valid email")
else:
    print("invalid email")