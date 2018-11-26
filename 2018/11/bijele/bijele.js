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
  const pieces = [1, 1, 2, 2, 2, 8];
  const diff = lines[0]
    .split(" ")
    .map(s => parseInt(s))
    .map((n, i) => pieces[i] - n)
    .join(" ");

  output(diff);
});
