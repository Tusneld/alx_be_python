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
base_message = f"'{task}' is a **{priority} priority** task"

# Use Match Case to determine the core recommendation based on priority
match priority:
    case 'high':
        recommendation = base_message + "."
    case 'medium':
        recommendation = base_message + ". Aim to start it soon."
    case 'low':
        recommendation = base_message + ". Consider completing it when you have free time."
    case _:
        # Default case for invalid priority input
        recommendation = f"'{task}' has an unrecognized priority level (**{priority}**)."

# Use an if statement to modify the reminder if the task is time-bound
if time_bound == 'yes':
    # This message is added to the base recommendation for high priority tasks
    # or overwrites it for others to emphasize urgency.
    if priority == 'high':
        final_reminder = recommendation.replace(".", " that requires **immediate attention today!**")
    elif priority in ['medium', 'low']:
        final_reminder = f"**URGENT**: {base_message} and it's time-bound! Try to complete it today."
    else:
        # Fallback for time-bound task with invalid priority
        final_reminder = f"Reminder: '{task}' is time-bound. Action required!"
else:
    # Use the recommendation as is if it's not time-bound
    final_reminder = recommendation

# Print the final customized reminder
print("\nReminder:", final_reminder)