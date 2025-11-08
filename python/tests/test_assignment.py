import pytest
from python.tests.tax_calc_starter import compute_taxes

def valid_input():
    return {
        "gross_income": 48000,
        "expenses": 3200,
        "miles": 9500,
        "mileage_rate": 0.70,
        "se_rate": 0.153,
        "income_rate": 0.12,
    }

def test_function_exists():
    assert callable(compute_taxes)

def test_negative_inputs_raise():
    data = valid_input()
    data["gross_income"] = -1
    with pytest.raises(Exception):
        compute_taxes(data)

def test_structure_of_output():
    result = compute_taxes(valid_input())
    assert isinstance(result, dict)
    for key in [
        "mileage_deduction",
        "total_deductions",
        "net_income",
        "se_tax",
        "income_tax",
        "total_tax",
        "effective_rate",
    ]:
        assert key in result, f"Missing key: {key}"
