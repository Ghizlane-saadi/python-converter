def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("---   Temperaturwandler ---")
celsius = float(input("Geben Sie den Wert in Prozent ein : "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}C = {fahrenheit}F")
