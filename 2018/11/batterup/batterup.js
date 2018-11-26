/*eslint no-console: "off"*/

const readline = require("readline");
const output = console.log.bind(console);

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
  const average = lines[1]
    .split(" ")
    .map(s => parseInt(s))
    .filter(n => n !== -1)
    .reduce((total, n, i, arr) => total + (n * 1) / arr.length, 0);

  output(average);
});
