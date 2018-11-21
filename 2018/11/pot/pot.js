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
  const output = lines
    .slice(1)
    .map(line => parseInt(line.slice(0, -1)) ** parseInt(line.slice(-1)))
    .reduce((a, b) => a + b);
  console.log(output);
});
