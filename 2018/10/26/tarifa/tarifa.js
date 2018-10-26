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
  const [X, N, ...P] = numbers;
  console.log(X + (X * N - P.reduce((a, b) => a + b)));
});
