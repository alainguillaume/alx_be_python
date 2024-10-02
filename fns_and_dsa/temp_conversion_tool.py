FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9) * (fahrenheit - 32)
    return FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5) * (celsius + 32)
    return CELSIUS_TO_FAHRENHEIT_FACTOR

# while True:
temperature = int(input("Enter the temperature to convert:"))
choice = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
if choice == 'C':
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
elif choice == 'F':
     print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
        
