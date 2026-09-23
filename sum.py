numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

total = 0

for n in numbers:
    total = total + n

average = total / 10

print("List =", numbers)
print("Sum =", total)
print("Average =", average)