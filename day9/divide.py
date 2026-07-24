
try:
    num1 = int(input("enter first number :"))
    num2 = int(input("enter second number : "))
    print(num1/num2)
except ZeroDivisionError:
    print("Cannot divide by zero.")
