n1 = int(input("enter n1 : "))
n2 = int(input("enter n2 : "))
n3 = int(input("enter n3 : "))

def max(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3

print("maximum number is ",max(n1,n2,n3))  
