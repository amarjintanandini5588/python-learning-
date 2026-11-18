numbers = [10, 5, 20, 8, 15]

largest = numbers[0]
second_largest = numbers[0]
for n in numbers:
    if n>largest:
        second_largest=largest
        largest=n
    elif n>second_largest:
        second_largest=n

print(largest)
print(second_largest)