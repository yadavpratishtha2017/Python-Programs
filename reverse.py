numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

reverse_list = []

for i in range(n - 1, -1, -1):
    reverse_list.append(numbers[i])

print("Original list:", numbers)
print("Reversed list:", reverse_list)