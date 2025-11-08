import { describe, it, expect } from "vitest";
import { computeTaxes } from "../tax_calc_starter";

const validInput = () => ({
  gross_income: 48000,
  expenses: 3200,
  miles: 9500,
  mileage_rate: 0.70,
  se_rate: 0.153,
  income_rate: 0.12,
});

describe("assignment", () => {
  it("function exists", () => {
    expect(typeof computeTaxes).toBe("function");
  });

  it("negative inputs should throw", () => {
    const bad = validInput();
    (bad as any).gross_income = -1;
    expect(() => computeTaxes(bad)).toThrow();
  });

  it("structure of output", () => {
    const out = computeTaxes(validInput());
    const keys = [
      "mileage_deduction",
      "total_deductions",
      "net_income",
      "se_tax",
      "income_tax",
      "total_tax",
      "effective_rate",
    ];
    expect(typeof out).toBe("object");
    for (const k of keys) expect(out).toHaveProperty(k);
  });
});
