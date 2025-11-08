from tax_calc_starter import compute_taxes

if __name__ == "__main__":
    data = {
        "gross_income": 48000,
        "expenses": 3200,
        "miles": 9500,
        "mileage_rate": 0.70,
        "se_rate": 0.153,
        "income_rate": 0.12,
    }
    result = compute_taxes(data)

    # Format and print output
    print(f"Mileage Deduction: ${result['mileage_deduction']:,.2f}")
    print(f"Total Deductions: ${result['total_deductions']:,.2f}")
    print(f"Net Income: ${result['net_income']:,.2f}")
    print(f"Self-Employment Tax: ${result['se_tax']:,.2f}")
    print(f"Income Tax: ${result['income_tax']:,.2f}")
    print(f"Total Tax: ${result['total_tax']:,.2f}")
    print(f"Effective Tax Rate: {result['effective_rate']:.2f}%")
