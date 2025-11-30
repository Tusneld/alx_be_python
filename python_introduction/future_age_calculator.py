# Prompt the user to enter their current age
# input() displays the message and waits for user input
# int() converts the user's input from string to integer
current_age = int(input("How old are you? "))

# Calculate the user's age in the year 2050
# We add 27 years because 2050 - 2023 = 27 years difference
# future_age stores the calculated age in 2050
future_age = current_age + 27

# Print the calculated future age
# This tells the user how old they will be in 2050
print(f"In 2050, you will be {future_age} years old")