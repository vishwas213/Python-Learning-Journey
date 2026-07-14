numbers = list(map(int , input("enter you list : ").split()))
count = 0
for i in numbers:
    count = count + i
avg = count/len(numbers)

print(avg)