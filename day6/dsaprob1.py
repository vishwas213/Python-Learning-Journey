number = list(map(int, input("enyer your list : ").slice()))

def second_largest(number):
    largest = number[0]
    second = number[0]

    for num in number:
        if num>largest :
            second= largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second


numbers = [10, 5, 20, 30, 15]

result = second_largest(numbers)

print("Second Largest =", result)
