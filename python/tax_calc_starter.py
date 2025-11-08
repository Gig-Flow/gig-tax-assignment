def compute_taxes(inputs):
    """
    Compute taxes for gig workers based on income, expenses, and mileage.
    
    Args:
        inputs (dict): Dictionary containing:
            - gross_income: Total income earned
            - expenses: Business expenses
            - miles: Business miles driven
            - mileage_rate: IRS mileage rate per mile
            - se_rate: Self-employment tax rate
            - income_rate: Income tax rate
    
    Returns:
        dict: Dictionary containing all computed tax values
    
    Raises:
        ValueError: If any input is negative
    """
    # Validate inputs - no negative values allowed
    for key, value in inputs.items():
        if value < 0:
            raise ValueError(f"{key} cannot be negative")
    
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
    
    # Calculate net income
    net_income = gross_income - total_deductions
    
    # Calculate self-employment tax (on net income)
    se_tax = net_income * se_rate
    
    # Calculate income tax (on net income after SE tax deduction)
    income_tax = (net_income - se_tax) * income_rate
    
    # Calculate total tax
    total_tax = se_tax + income_tax
    
    # Calculate effective tax rate (as a percentage)
    effective_rate = (total_tax / gross_income) * 100 if gross_income > 0 else 0
    
    # Return all computed values
    return {
        "mileage_deduction": mileage_deduction,
        "total_deductions": total_deductions,
        "net_income": net_income,
        "se_tax": se_tax,
        "income_tax": income_tax,
        "total_tax": total_tax,
        "effective_rate": effective_rate,
    }
