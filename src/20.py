def calculate_total_expenses(incomes):
    total = 0
    
    for income in incomes:
        if isinstance(income, int) or isinstance(income, float):
            total += income
        elif isinstance(income, str):
            try:
                total += sum(map(float, income.split()))
            except ValueError:
                print(f"Invalid input: {income}")
    
    return total

# Example usage
incomes = [10000, 25000, -3500, "450", 600]
print("Total Expenses:", calculate_total_expenses(incomes))
