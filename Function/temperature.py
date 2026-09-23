def celsius_to_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f

c = float(input("Enter temperature in Celsius: "))

f = celsius_to_fahrenheit(c)

print("Temperature in Fahrenheit:", f)