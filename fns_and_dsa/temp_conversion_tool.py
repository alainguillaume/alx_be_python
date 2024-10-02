# Conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32

# Main loop for temperature conversion
while True:
    temperature = float(input("Enter the temperature to convert: "))
    choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if choice == 'C':
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature):.2f}°F")
    elif choice == 'F':
        print(f"{temperature}°F is {convert_to_celsius(temperature):.2f}°C")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")
    
    # Option to continue or exit
    continue_choice = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        break
