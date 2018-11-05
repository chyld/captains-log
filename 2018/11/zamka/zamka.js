const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const numbers = [];

rl.on("line", line => {
  numbers.push(parseInt(line));
});

rl.on("close", () => {
  const [L, D, X] = numbers;
  const N = getValue(L, D + 1, +1, X);
  const M = getValue(D, L - 1, -1, X);
  console.log(N);
  console.log(M);
});

function getValue(start, stop, step, value) {
  for (let i = start; i !== stop; i += step) {
    const v = String(i)
      .split("")
      .map(c => parseInt(c))
      .reduce((a, n) => a + n);
    if (v === value) {
      return i;
    }
  }
}
