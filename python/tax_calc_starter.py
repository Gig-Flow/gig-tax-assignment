# TODO: Implement your logic here (no solution provided)
# Suggested: define compute_taxes(inputs: dict) -> dict

def compute_taxes(inputs: dict) -> dict:
    """
    Compute estimated gig worker taxes based on simplified IRS-like logic.

    Args:
        inputs (dict): Dictionary with keys:
            - gross_income (float): total gig earnings
            - expenses (float): total deductible expenses
            - miles (float): total business miles
            - mileage_rate (float): IRS mileage rate per mile
            - se_rate (float): self-employment tax rate
            - income_rate (float): federal income tax rate

    Returns:
        dict: {
            mileage_deduction,
            total_deductions,
            net_income,
            se_tax,
            income_tax,
            total_tax,
            effective_rate
        }
    """

    # Validate input fields
    required_fields = ["gross_income", "expenses", "miles", "mileage_rate", "se_rate", "income_rate"]
    for field in required_fields:
        if field not in inputs:
            raise ValueError(f"Missing required input field: '{field}'")

    gross_income = float(inputs["gross_income"])
    expenses = float(inputs["expenses"])
    miles = float(inputs["miles"])
    mileage_rate = float(inputs["mileage_rate"])
    se_rate = float(inputs["se_rate"])
    income_rate = float(inputs["income_rate"])

    # Validate no negative values
    if gross_income < 0 or expenses < 0 or miles < 0 or mileage_rate < 0 or se_rate < 0 or income_rate < 0:
        raise ValueError("All input values must be non-negative")

    # Deductions
    mileage_deduction = miles * mileage_rate
    total_deductions = mileage_deduction + expenses

    # Income after deductions
    net_income = max(gross_income - total_deductions, 0)

    # Taxes
    se_tax = net_income * se_rate
    income_tax = net_income * income_rate
    total_tax = se_tax + income_tax

    # Effective tax rate
    effective_rate = (total_tax / gross_income) if gross_income > 0 else 0

    return {
        "mileage_deduction": round(mileage_deduction, 2),
        "total_deductions": round(total_deductions, 2),
        "net_income": round(net_income, 2),
        "se_tax": round(se_tax, 2),
        "income_tax": round(income_tax, 2),
        "total_tax": round(total_tax, 2),
        "effective_rate": round(effective_rate, 4),
    }
