# Rules:

# At least 8 characters
# Contains at least one digit
# Contains at least one alphabet

password = input("enter your password : ")

lenght = len(password)
digit = password.isdigit
alpha = password.isalpha

if lenght >= 8 and digit >=1 and alpha>=1 :
    print("strong password ")
else:
    print("weak password ")