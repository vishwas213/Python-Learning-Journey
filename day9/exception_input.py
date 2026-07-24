while True :
    try:
        number = int(input("enter your number : "))
        break
    except ValueError:
        print("enter valid number ")

