# TODO: Implement your logic here (no solution provided)
# Suggested: define compute_taxes(inputs: dict) -> dict

def compute_taxes(inputs):
    """
    Compute tax calculations for gig workers.
    
    Args:
        inputs: Dictionary containing:
            - gross_income: Total income before deductions
            - expenses: Business expenses
            - miles: Business miles driven
            - mileage_rate: Rate per mile
            - se_rate: Self-employment tax rate
            - income_rate: Income tax rate
    
    Returns:
        Dictionary with computed values:
            - mileage_deduction: Deduction from miles
            - total_deductions: Sum of expenses and mileage deduction
            - net_income: Income after deductions
            - se_tax: Self-employment tax
            - income_tax: Income tax
            - total_tax: Sum of SE and income tax
            - effective_rate: Total tax as percentage of gross income
    
    Raises:
        ValueError: If any input value is negative
    """
    # Validate inputs - no negative values allowed
    for key, value in inputs.items():
        if value < 0:
            raise ValueError(f"Input '{key}' cannot be negative: {value}")
    
    # Extract input values
    gross_income = inputs["gross_income"]
    expenses = inputs["expenses"]
    miles = inputs["miles"]
    mileage_rate = inputs["mileage_rate"]
    se_rate = inputs["se_rate"]
    income_rate = inputs["income_rate"]
    
    # Calculate mileage deduction
    mileage_deduction = miles * mileage_rate
    
    # Calculate total deductions
    total_deductions = expenses + mileage_deduction
    
    # Calculate net income (gross income minus deductions)
    net_income = gross_income - total_deductions
    
    # Calculate self-employment tax
    se_tax = net_income * se_rate
    
    # Calculate income tax
    income_tax = net_income * income_rate
    
    # Calculate total tax
    total_tax = se_tax + income_tax
    
    # Calculate effective tax rate (total tax / gross income)
    effective_rate = (total_tax / gross_income) * 100 if gross_income > 0 else 0
    
    return {
        "mileage_deduction": mileage_deduction,
        "total_deductions": total_deductions,
        "net_income": net_income,
        "se_tax": se_tax,
        "income_tax": income_tax,
        "total_tax": total_tax,
        "effective_rate": effective_rate,
    }
