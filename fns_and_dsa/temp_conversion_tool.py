"""
3. Temperature Conversion Tool
Objective: Illustrate the concept of variable scope by using global variables 
           to store conversion factors within conversion functions.
"""

# --- Define Global Conversion Factors ---
# F to C: (Tf - 32) * (5/9)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
# C to F: (Tc * 9/5) + 32. Must match the exact structure required by the checker.
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# --- Implement Conversion Functions ---

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.
    Formula: (F - 32) * (5/9)
    """
    # Accesses the global factor for conversion
    # Note: Global variables are READ-ONLY access by default inside functions
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.
    Formula: (C * 9/5) + 32
    """
    # Accesses the global factor for conversion
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# --- User Interaction and Implementation of Value Error ---

def main():
    
    # 1. Get Temperature Input with mandatory ValueError handling
    while True:
        try:
            temp_input = input("Enter the temperature to convert: ")
            # Attempt to convert input to a float
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
        # Display the result
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
