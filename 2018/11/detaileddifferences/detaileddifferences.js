/*eslint no-console: "off"*/

function* lineGenerator() {
  for (const line of lines) yield line;
}

const readline = require("readline");
const output = console.log.bind(console);
const range = size => Array.from({ length: size }, (v, i) => i);
const lineIterator = lineGenerator();

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
  lineIterator.next();

  for (let a of lineIterator) {
    let b = lineIterator.next().value;

    a = [...a];
    b = [...b];

    const diff = a.map((ac, i) => (ac === b[i] ? "." : "*"));
    output(a.join("") + "\n" + b.join("") + "\n" + diff.join("") + "\n");
  }
});
