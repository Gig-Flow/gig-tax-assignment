// TODO: Implement your logic here (no solution provided)
// Suggested: export function computeTaxes(inputs: Record<string, number>): Record<string, number>

export function computeTaxes(inputs: Record<string, number>): Record<string, number> {
  // Extract inputs
  const {
    gross_income,
    expenses,
    miles,
    mileage_rate,
    se_rate,
    income_rate,
  } = inputs;

  // Validate inputs (no negatives)
  if (gross_income < 0 || expenses < 0 || miles < 0 || 
      mileage_rate < 0 || se_rate < 0 || income_rate < 0) {
    throw new Error("All inputs must be non-negative");
  }

  // Calculate mileage deduction
  const mileage_deduction = miles * mileage_rate;

  // Calculate total deductions
  const total_deductions = expenses + mileage_deduction;

  // Calculate net income (taxable income)
  const net_income = gross_income - total_deductions;

  // Calculate self-employment tax
  const se_tax = net_income * se_rate;

  // Calculate income tax
  const income_tax = net_income * income_rate;

  // Calculate total tax
  const total_tax = se_tax + income_tax;

  // Calculate effective tax rate (as a percentage)
  const effective_rate = gross_income > 0 ? (total_tax / gross_income * 100) : 0;

  // Return object with all computed values
  return {
    mileage_deduction,
    total_deductions,
    net_income,
    se_tax,
    income_tax,
    total_tax,
    effective_rate,
  };
}
