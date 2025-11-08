# Tax Computation Tool - Python Implementation

## Approach

This implementation calculates taxes for gig workers by first computing deductions (expenses + mileage), then determining net income by subtracting total deductions from gross income. Taxes are calculated on net income: self-employment tax at 15.3% and income tax at 12%. The effective tax rate represents total tax as a percentage of gross income. Input validation ensures all values are non-negative, raising a ValueError for invalid inputs. The CLI formats results with currency formatting for financial clarity.

