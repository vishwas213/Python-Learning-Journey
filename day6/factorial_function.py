n = int(input("enter your number : "))

def factorial(n):
    count = 1

    while n>= 1: 
        count = count * n
        n = n -1
    
    return count

result = factorial(n)

print(result)
