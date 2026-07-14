numbers = list(map(int , input("enter you list : ").split()))
count = 0
for i in numbers :
    if i>= 0 :
        count = count + 1

print(count)