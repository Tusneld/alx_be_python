# Get user input for monthly financial details
# float() converts the input to a decimal number to handle currency values
# monthly_income stores the user's total monthly income
monthly_income = float(input("Enter your monthly income: "))
# monthly_expenses stores the user's total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings by subtracting expenses from income
# monthly_savings stores the amount saved each month
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with 5% interest
# First part: monthly_savings * 12 calculates total savings without interest
# Second part: (monthly_savings * 12 * 0.05) calculates the 5% interest
# projected_savings stores the total savings after one year with interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display the monthly savings result
# :.0f formats the number to show no decimal places (whole dollars)
print(f"Your monthly savings are ${monthly_savings:.0f}.")

# Display the projected annual savings with interest
# This shows how much the user will have saved after one year
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")