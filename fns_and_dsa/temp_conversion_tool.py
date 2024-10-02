# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def main():
    while True:
        user_input = input("Enter a temperature (e.g., 32F, 0C): ").strip()
        
        try:
            # Check if the last character is 'F' or 'C' for the temperature unit
            if user_input[-1].upper() == 'F':
                # Extract the numeric part
                temperature = float(user_input[:-1])
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}F is {converted_temp:.2f}C")
                break

            elif user_input[-1].upper() == 'C':
                temperature = float(user_input[:-1])
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}C is {converted_temp:.2f}F")
                break

            else:
                raise ValueError("Invalid temperature unit. Please enter a temperature followed by 'F' or 'C'.")

        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
