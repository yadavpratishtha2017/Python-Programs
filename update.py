fruits = []
fruit1 = input("Enter a fruit name 1: ")
fruit2 = input("Enter a fruit name 2: ")
fruit3 = input("Enter a fruit name 3: ")
fruit4 = input("Enter a fruit name 4: ")
fruit5 = input("Enter a fruit name 5: ")

fruits.append(fruit1)
fruits.append(fruit2)       
fruits.append(fruit3)
fruits.append(fruit4)   
fruits.append(fruit5)

print(fruits)

print(fruits[1])
print(fruits[3])

fruits[4] = "mango"

print(fruits)