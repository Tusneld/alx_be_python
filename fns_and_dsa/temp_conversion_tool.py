"""
3. Temperature Conversion Tool
Objective: Illustrate the concept of variable scope by using global variables 
           to store conversion factors within conversion functions.
"""

# Define Global Conversion Factors (accessible by all functions)
# F to C: (Tf - 32) * (5/9)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9 
# C to F: (Tc * (9/5)) + 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit: float) -> float:
    """Converts a temperature from Fahrenheit to Celsius."""
    # Accesses the global factor for conversion
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float) -> float:
    """Converts a temperature from Celsius to Fahrenheit."""
    # Accesses the global factor for conversion
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # --- User Interaction and Validation ---
    
    # 1. Get Temperature Input
    while True:
        try:
            temp_input = input("Enter the temperature to convert: ")
            temperature = float(temp_input)
            break
        except ValueError:
            # Raise the specified error for non-numeric input
            raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    # 2. Get Unit Input
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ('C', 'F'):
            break
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    # 3. Perform and Display Conversion
    
    if unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temperature)
        # Display the result (ensuring the original input is used)
        print(f"{temperature}°F is {converted_temp}°C")
        
    elif unit == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        # Display the result
        print(f"{temperature}°C is {converted_temp}°F")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        # Catch and display the specific error raised in main()
        print(e)