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
  const map = lines[0].split(" ").reduce((map, word) => {
    const val = map.has(word) ? map.get(word) + 1 : 1;
    map.set(word, val);
    return map;
  }, new Map());

  const sum = [...map.values()].reduce((a, b) => a + b);
  const length = map.size;
  const response = sum == length ? "yes" : "no";

  output(response);
});
