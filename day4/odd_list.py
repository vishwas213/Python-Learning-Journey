numbers = list(map(int , input("enter your list").split()))
odd = []

print("odd numbers are")

for i in numbers :
    if i % 2 == 1 :
        odd.append(i)

print(odd)