"""
2. Explore datetime Module
Objective: Familiarize yourself with Python's datetime module for handling dates and times.
"""
# Import the necessary classes from the datetime module
from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in a specified format."""
    # Part 1: Display the Current Date and Time
    current_date = datetime.now()
    
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    
    # Return the current date object for use in the next function
    return current_date

def calculate_future_date(current_date):
    """
    Calculates a future date by adding a user-specified number of days.
    
    Parameters:
    current_date (datetime): The starting date object.
    """
    # Part 2: Calculate a Future Date
    while True:
        try:
            # Prompt the user for the number of days
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            
            # Use timedelta to represent the duration
            time_difference = timedelta(days=days_to_add)
            
            # Calculate the future date
            future_date = current_date + time_difference
            
            # Print the future date in the format "YYYY-MM-DD"
            print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
            
            # Exit the loop on successful calculation
            break
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a valid whole number for the number of days.")

# Main execution block
if __name__ == "__main__":
    # Call the function to display the current date/time and get the date object
    current_date = display_current_datetime()
    
    # Call the function to calculate and display the future date
    calculate_future_date(current_date)