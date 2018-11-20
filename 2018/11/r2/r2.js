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
  const [a, mean] = lines[0].split(" ").map(s => parseInt(s));
  const b = mean * 2 - a;
  console.log(b);
});
