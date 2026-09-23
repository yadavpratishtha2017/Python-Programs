numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter integer: "))
    numbers.append(num)

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("List after removing duplicates:", unique)