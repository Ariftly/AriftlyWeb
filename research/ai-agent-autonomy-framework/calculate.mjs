const targets = [0.95, 0.99, 0.999];
const steps = [5, 10, 20, 50, 100];
const perStepValues = [0.98, 0.99, 0.995, 0.999];
const fixedSteps = [10, 20, 50];

console.log("series,target_end_to_end_reliability,per_step_reliability,steps,result");

for (const target of targets) {
  for (const count of steps) {
    console.log(`required_per_step,${target},,${count},${(target ** (1 / count)).toFixed(6)}`);
  }
}

for (const perStep of perStepValues) {
  for (const count of fixedSteps) {
    console.log(`fixed_per_step,,${perStep},${count},${(perStep ** count).toFixed(6)}`);
  }
}

console.log("\nzero_failure_trials,approx_95pct_upper_failure_probability");
for (const trials of [100, 300, 1000, 3000, 10000]) {
  console.log(`${trials},${(3 / trials).toFixed(4)}`);
}
