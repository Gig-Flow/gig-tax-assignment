# Tax Computation Implementation

## Approach

This implementation calculates taxes for U.S. gig workers using standard IRS rules:
- Mileage deduction is computed by multiplying the business miles by the mileage rate
- Total deductions is expenses added to mileage deduction
- Net income is gross income minus total deductions
- Self-employment tax is calculated on 92.35% of net income (IRS standard)
- Income tax is calculated on net income minus half of self-employment tax (deductible portion)
- All inputs are validated to ensure no negative values
- Output is formatted for clarity with proper dollar amounts and percentages

The code inclues comprehensive input validation to handle edge cases.
