numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(44 in numbers)
numbers.append(44)
print(44 in numbers)
numbers.remove(44)
print(44 in numbers)

print("number of numbers: " + str(len(numbers)))