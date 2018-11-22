/*eslint no-console: "off"*/

const readline = require("readline");
const output = console.log.bind(console);
const range = size => Array.from({ length: size }, (v, i) => i);
function* lineGenerator() {
  for (const line of lines) yield line;
}
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
  const n = lineIterator.next().value * 1;
  const response = range(n).map(_ =>
    countCities(lineIterator.next().value * 1)
  );
  output(response.join("\n"));
});

function countCities(num) {
  const set = range(num).reduce((set, _) => {
    const city = lineIterator.next().value;
    set.add(city);
    return set;
  }, new Set());
  return set.size;
}
