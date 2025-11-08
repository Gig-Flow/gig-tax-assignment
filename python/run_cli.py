from python.tax_calc_starter import compute_taxes

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
    print(result)
