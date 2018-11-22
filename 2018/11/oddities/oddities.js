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
  const response = lines
    .slice(1)
    .map(line => parseInt(line))
    .map(n => n + " is " + ["even", "odd"][Math.abs(n) % 2])
    .join("\n");
  console.log(response);
});
