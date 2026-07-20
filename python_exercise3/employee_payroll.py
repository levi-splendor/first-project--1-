def calculate_payroll(employees):
    payroll = {}
    
    for employee in employees:
        name = employee["name"]
        hours = employee["hours_worked"]
        rate = employee["hourly_rate"]
        
        # Calculate regular pay (max 40 hours)
        regular_pay = min(40, hours) * rate
        
        # Calculate overtime pay (1.5x rate for hours over 40)
        overtime_hours = max(0, hours - 40)
        overtime_pay = overtime_hours * rate * 1.5

        total_pay = regular_pay + overtime_pay
        
        payroll[name] = total_pay
    return payroll
def highest_paid(payroll):
    if not payroll:
        return None  # No employees
    
    # Find the name with the maximum pay value
    highest_name = max(payroll, key=payroll.get)
    return highest_name

    # Sample data
employees = [
    {"name": "Alice", "hours_worked": 45, "hourly_rate": 20},
    {"name": "Bob", "hours_worked": 35, "hourly_rate": 25},
    {"name": "Charlie", "hours_worked": 50, "hourly_rate": 18}
]

payroll = calculate_payroll(employees)
print(payroll)

print("Highest paid:", highest_paid(payroll))
