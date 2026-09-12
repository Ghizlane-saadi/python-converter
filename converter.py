def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("---  Temperature Converter ---")
celsius = float(input("Enter the value as a percentage : "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}C = {fahrenheit}F")
