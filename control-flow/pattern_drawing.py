""""
3. Drawing Patterns with Nested Loops
Objective: Utilize while loops and nested for loops to draw a simple text-based pattern.

Task Description:

Develop a Python script named pattern_drawing.py. This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).

Instructions:

Prompt User for Pattern Size:

Ask the user to input a positive integer that represents the size of the pattern (i.e., the length of each side of the square): Enter the size of the pattern:.
Draw the Pattern:

First, use a while loop to iterate through each row of the pattern.
Inside the while loop, use a for loop to print asterisks (*) side by side without advancing to a new line (you can use print("*", end="") for this).
After completing each row, print a newline character to move to the next row.
Continue until the pattern forms a square of the inputted size.
"""

# Prompt User for Pattern Size

try:
    size = int(input("Enter the size of the pattern:"))
    if size <= 0:
        # Handle non-positive input gracefully
        print("Size must be a positive integer.")
        exit()
except ValueError:
    # Handle non-integer input gracefully
    print("Invalid input. Please enter a positive integer.")
    exit()

# Initialize row counter for the while loop
row = 0

# Draw the Pattern
# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks for the current row (columns)
    for col in range(size):
        # Print an asterisk and stay on the same line
        print("*", end="")

    # After the for loop finishes, print a newline to move to the next row
    print()

    # Increment the row counter
    row += 1
