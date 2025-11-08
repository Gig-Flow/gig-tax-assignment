# Tax Computation Tool (Python)

This script computes estimated U.S. gig worker taxes for 2025 using:
- Gross income, expenses, and mileage
- Standard mileage rate ($0.70/mile)
- Self-employment tax (15.3%)
- Federal income tax (12%)

### Approach
1. Validate inputs (no negatives or missing values).
2. Calculate mileage deduction, total deductions, and net income.
3. Compute self-employment and income taxes.
4. Output total tax and effective tax rate.
5. CLI prints formatted dollar values for clarity.

### Run
```bash
cd python
python3 tax_calc.py
