import { computeTaxes } from "./tax_calc_starter";

const res = computeTaxes({
  gross_income: 48000,
  expenses: 3200,
  miles: 9500,
  mileage_rate: 0.70,
  se_rate: 0.153,
  income_rate: 0.12,
});

const fmt = (n: number) => n.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });

console.log(`Mileage Deduction: $${fmt(res.mileage_deduction)}`);
console.log(`Total Deductions: $${fmt(res.total_deductions)}`);
console.log(`Net Income: $${fmt(res.net_income)}`);
console.log(`Self-Employment Tax: $${fmt(res.se_tax)}`);
console.log(`Income Tax: $${fmt(res.income_tax)}`);
console.log(`Total Tax: $${fmt(res.total_tax)}`);
console.log(`Effective Tax Rate: ${(res.effective_rate * 100).toFixed(2)}%`);
