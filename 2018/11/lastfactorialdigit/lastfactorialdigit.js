/*eslint no-console: "off"*/

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

const lines = [];

rl.on("line", line => {
  lines.push(line);
});

rl.on("close", () => {
  const factorials = lines
    .slice(1)
    .map(line => parseInt(line))
    .map(factorial)
    .map(String)
    .map(s => s.slice(-1));
  const output = factorials.join("\n");
  console.log(output);
});

function factorial(n) {
  if ([1, 1][n]) return [1, 1][n];
  return n * factorial(n - 1);
}
