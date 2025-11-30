"""
2. Multiplication Table Generator
Objective: Use a for loop to generate and print the multiplication table for a given number.
Task Description:

Create a Python script named multiplication_table.py. This script will ask the user to enter a number, then use a for loop to print the multiplication table for that number from 1 to 10.

Instructions:

Prompt User for a Number:

Ask the user to input a number for which they want to see the multiplication table: Enter a number to see its multiplication table:.
Save it in a variable name number
Generate and Print the Multiplication Table:

Use a for loop to iterate through the numbers 1 to 10.
For each iteration, calculate the product of the user’s number and the iterator (the current number in the loop from 1 to 10).
Print each line of the multiplication table in the format: “X * Y = Z”, where X is the user’s number, Y is the current number in the loop, and Z is the product.
Example Interaction:

If the user inputs 5, the output should be:

Enter a number to see its multiplication table: 5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
This task is designed to reinforce the concept of for loops by applying them in a practical scenario that generates a multiplication table. Through this exercise, students will learn how loops can significantly simplify the process of performing repetitive tasks, enhancing their understanding of looping constructs in Python.
"""
# Prompt user for a number
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    # Exit if input is invalid
    exit()

# Generate and print the multiplication table using a for loop
print(f"Multiplication table for {number}:")
# The range function generates numbers from the start (1) up to, but not including, the stop (11)
for i in range(1, 11):
    product = number * i
    # Print each line in the format "X * Y = Z"
    print(f"{number} * {i} = {product}")