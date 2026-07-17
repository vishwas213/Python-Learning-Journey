numbers = list(map(int,input("enter you list : ").split()))

def avg(numbers):
    ttl = sum(numbers)
    total = len(numbers)

    avg = ttl/total
    return avg

print("avg of list is ",avg(numbers))