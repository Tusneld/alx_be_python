"""

4. Personal Daily Reminder

Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

Task Description:

Develop a script named daily_reminder.py. This script will ask the user for a single task, its priority level, and if it is time-sensitive. The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.

Instructions:

Prompt for a Single Task:

Ask the user to input a task description and save it into a task variable
Prompt for the task’s priority (high, medium, low) and save it into a priority variable
In a time_bound variable, Ask if the task is time-bound (yes or no)
Process the Task Based on Priority and Time Sensitivity:

Use a Match Case statement to react differently based on the task’s priority.
Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
Provide a Customized Reminder:

Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
A message should be ‘that requires immediate attention today!’
Example Interaction and Output:

Enter your task: Finish project report
Priority (high/medium/low): high
Is it time-bound? (yes/no): yes

Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
Or, for a non-time-bound task:

Enter your task: Read a book
Priority (high/medium/low): low
Is it time-bound? (yes/no): no

Note: 'Read a book' is a low priority task. Consider completing it when you have free time.
"""
# Prompt for a single task and its details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the base reminder message
final_reminder_text = ""

# Process the Task Based on Priority and Time Sensitivity using Match Case
match priority:
    case 'high':
        base_message = f"'{task}' is a high priority task"
    case 'medium':
        base_message = f"Note: '{task}' is a medium priority task"
    case 'low':
        base_message = f"Note: '{task}' is a low priority task"
    case _:
        # Default case for unrecognized priority
        base_message = f"'{task}' has an unrecognized priority ({priority})"

# Use an if statement to modify the reminder if the task is time-bound.
if time_bound == 'yes' and priority == 'high':
    # Example 1 match: high priority and time-bound
    # If a high priority task is time-bound, add the immediate action clause
    immediate_action_clause = " that requires immediate attention today!"
    final_reminder_text = base_message + immediate_action_clause

elif time_bound == 'yes' and priority in ['medium', 'low']:
    # Treat medium/low time-bound tasks with urgency
    final_reminder_text = f"**Time-bound:** {base_message}. Try to complete it today!"

elif priority == 'low':
    # Example 2 match: low priority and not time-bound
    final_reminder_text = base_message + ". Consider completing it when you have free time."

else:
    # Handles 'high' or 'medium' priority that is not time-bound, or any other case.
    final_reminder_text = base_message + "."


# Provide a Customized Reminder using the required print format
# Ensure the output string starts with "Reminder: "
print(f"\nReminder: {final_reminder_text}")
