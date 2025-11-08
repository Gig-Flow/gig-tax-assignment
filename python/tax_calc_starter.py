def compute_taxes(inputs):
    """
    Compute taxes for U.S. gig workers based on income, expenses, and mileage.

    Args:
        inputs: Dictionary containing:
            - gross_income: Total gross income
            - expenses: Business expenses
            - miles: Business miles driven
            - mileage_rate: IRS mileage rate
            - se_rate: Self-employment tax rate
            - income_rate: Income tax rate

    Returns:
        Dictionary with computed tax values
    """
    # Validate inputs - no negative values
    for key, value in inputs.items():
        if value < 0:
            raise ValueError(f"Invalid input: {key} cannot be negative")

    # Extract inputs
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

    # Calculate self-employment tax (on 92.35% of net income)
    se_tax = net_income * 0.9235 * se_rate

    # Calculate income tax (can deduct half of SE tax from taxable income)
    taxable_income = net_income - (se_tax / 2)
    income_tax = taxable_income * income_rate

    # Calculate total tax
    total_tax = se_tax + income_tax

    # Calculate effective tax rate
    effective_rate = (total_tax / gross_income * 100) if gross_income > 0 else 0

    return {
        "mileage_deduction": mileage_deduction,
        "total_deductions": total_deductions,
        "net_income": net_income,
        "se_tax": se_tax,
        "income_tax": income_tax,
        "total_tax": total_tax,
        "effective_rate": effective_rate,
    }
