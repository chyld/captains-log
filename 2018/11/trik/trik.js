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
  const final = [...lines[0]].reduce((position, fn) => fns[fn](position), 1);
  output(final);
});

const fns = {
  A,
  B,
  C
};

function A(x) {
  if (x === 1) return 2;
  if (x === 2) return 1;
  return x;
}

function B(x) {
  if (x === 2) return 3;
  if (x === 3) return 2;
  return x;
}

function C(x) {
  if (x === 1) return 3;
  if (x === 3) return 1;
  return x;
}
