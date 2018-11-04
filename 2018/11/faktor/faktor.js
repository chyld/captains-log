const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let A, I;

rl.on("line", line => {
  [A, I] = line.split(" ").map(c => parseInt(c));
});

rl.on("close", () => {
  const discount = 0.99;
  const result = Math.ceil(A * (I - discount));
  console.log(result);
});
