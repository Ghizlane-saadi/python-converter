def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("--- محول درجات الحرارة ---")
celsius = float(input("أدخل الدرجة بالمئوية: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}C تساوي {fahrenheit}F")
