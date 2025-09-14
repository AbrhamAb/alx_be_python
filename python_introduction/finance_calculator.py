# Prompt user for financial details (strings)
monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

# Calculate monthly savings (convert inputs to floats)
monthly_savings = float(monthly_income) - float(monthly_expenses)

# Project annual savings with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display results (match example formatting)
print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
