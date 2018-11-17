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
  const count = lines[1]
    .split(" ")
    .map(s => parseInt(s))
    .reduce((total, n) => total + Number(n < 0), 0);
  console.log(count);
});
