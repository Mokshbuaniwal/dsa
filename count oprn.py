def ctof(c):
    return (c * 9/5) + 32   # 3 operations: *, /, +

celsius = int(input("Enter temperature in Celsius: "))
fahrenheit = ctof(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")