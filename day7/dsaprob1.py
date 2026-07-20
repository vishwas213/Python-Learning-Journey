numbers = list(map(int, input("enter your list : ").split()))

result = {
    "Largest": numbers[0],
    "Smallest": numbers[0]
}

for num in numbers:
    if num > result["Largest"]:
        result["Largest"] = num

    if num < result["Smallest"]:
        result["Smallest"] = num

print("Largest =", result["Largest"])
print("Smallest =", result["Smallest"])