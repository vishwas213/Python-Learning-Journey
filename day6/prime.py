# n = int(input("enter your number : "))

# def is_prime(n):
#     i = 1
#     while i<=n:
#         i = i+1
#         if n%i==0:
#             print("number is  prime : ")
#             return True
#         else:
#             print("number is non prime  : ")
#             return False
        
# # if is_prime(n) == True:
# #     print("number is prime number :")
# # else :
# #     print("number is non prime")

# print(is_prime(n))

n = int(input("Enter your number: "))

def is_prime(n):
    if n <= 1:
        return False

    i = 2

    while i < n:
        if n % i == 0:
            return False
        i = i + 1

    return True


if is_prime(n):
    print("Prime Number")
else:
    print("Not Prime")