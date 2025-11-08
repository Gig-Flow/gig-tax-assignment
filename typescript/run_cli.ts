import { computeTaxes } from "./tax_calc_starter";

const data = {
  gross_income: 48000,
  expenses: 3200,
  miles: 9500,
  mileage_rate: 0.70,
  se_rate: 0.153,
  income_rate: 0.12,
};

console.log(computeTaxes(data));
