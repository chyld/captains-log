const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let X;

rl.on("line", line => {
  X = parseFloat(line);
});

rl.on("close", () => {
  const ratio_mile_paces = 1e3 * (5280 / 4854);
  const result = Math.round(X * ratio_mile_paces);
  console.log(result);
});
