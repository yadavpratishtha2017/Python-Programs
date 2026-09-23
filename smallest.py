numbers = []

for i in range(7):
    n = int(input("Enter number: "))
    numbers.append(n)

small = numbers[0]
large = numbers[0]

for n in numbers:
    if n < small:
        small = n
    if n > large:
        large = n

print("Smallest =", small)
print("Largest =", large)