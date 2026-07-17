numbers = list(map(int , input("enter you list : ").split()))
even = []
print(" even numbers")

numbers.sort()
for i in numbers :
    if i % 2 == 0:
        even.append(i)
        
print(even)



