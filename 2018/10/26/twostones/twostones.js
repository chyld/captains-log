const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N = 0;

rl.on("line", line => {
  N = parseInt(line);
});

rl.on("close", () => {
  const result = { 0: "Bob", 1: "Alice" }[N % 2];
  console.log(result);
});
