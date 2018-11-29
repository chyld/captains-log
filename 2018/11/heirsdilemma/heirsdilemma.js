/*eslint no-console: "off"*/

const readline = require("readline");
const range = size => Array.from({ length: size }, (v, i) => i);

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
  const [l, u] = lines[0].split(" ").map(s => parseInt(s));
  const delta = u - l;
  const valid = range(delta + 1)
    .map(i => l + i)
    .filter(isLen6)
    .filter(allDifferent)
    .filter(allDivisible);

  console.log(valid.length);
});

function isLen6(n) {
  return String(n).length === 6;
}

function allDifferent(n) {
  return new Set(String(n)).size === 6;
}

function allDivisible(n) {
  return [...String(n)]
    .map(s => parseInt(s))
    .reduce((isGood, x) => isGood && n % x == 0, true);
}
