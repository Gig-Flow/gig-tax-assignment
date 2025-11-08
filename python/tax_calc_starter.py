#!/usr/bin/env python3

"""
Tax Computation Tool for U.S. Gig Workers — 2025
Author: <your name>
"""

def compute_taxes(inputs: dict) -> dict:
    """
    Computes U.S. self-employment and income taxes based on gig income data.
    """

    required_keys = [
        "gross_income", "expenses", "miles",
        "mileage_rate", "se_rate", "income_rate"
    ]
    for key in required_keys:
        if key not in inputs:
            raise ValueError(f"Missing input: {key}")
        if not isinstance(inputs[key], (int, float)):
            raise TypeError(f"{key} must be numeric")
        if inputs[key] < 0:
            raise ValueError(f"{key} cannot be negative")

    gross_income = inputs["gross_income"]
    expenses = inputs["expenses"]
    miles = inputs["miles"]
    mileage_rate = inputs["mileage_rate"]
    se_rate = inputs["se_rate"]
    income_rate = inputs["income_rate"]

    # 1️⃣ Mileage deduction
    mileage_deduction = miles * mileage_rate

    # 2️⃣ Total deductions
    total_deductions = expenses + mileage_deduction

    # 3️⃣ Net income
    net_income = max(gross_income - total_deductions, 0)

    # 4️⃣ Self-employment tax
    se_tax = net_income * se_rate

    # 5️⃣ Income tax
    income_tax = net_income * income_rate

    # 6️⃣ Total tax
    total_tax = se_tax + income_tax

    # 7️⃣ Effective tax rate (based on gross)
    effective_rate = total_tax / gross_income if gross_income > 0 else 0

    return {
        "mileage_deduction": round(mileage_deduction, 2),
        "total_deductions": round(total_deductions, 2),
        "net_income": round(net_income, 2),
        "se_tax": round(se_tax, 2),
        "income_tax": round(income_tax, 2),
        "total_tax": round(total_tax, 2),
        "effective_rate": round(effective_rate, 4),
    }


if __name__ == "__main__":
    # Scenario (2025)
    inputs = {
        "gross_income": 48000,
        "expenses": 3200,
        "miles": 9500,
        "mileage_rate": 0.70,
        "se_rate": 0.153,
        "income_rate": 0.12,
    }

    result = compute_taxes(inputs)

    print("=== U.S. Gig Worker Tax Computation (2025) ===")
    print(f"Mileage Deduction: ${result['mileage_deduction']:,.2f}")
    print(f"Total Deductions: ${result['total_deductions']:,.2f}")
    print(f"Net Income: ${result['net_income']:,.2f}")
    print(f"Self-Employment Tax: ${result['se_tax']:,.2f}")
    print(f"Income Tax: ${result['income_tax']:,.2f}")
    print(f"Total Tax: ${result['total_tax']:,.2f}")
    print(f"Effective Tax Rate: {result['effective_rate']*100:.2f}%")
