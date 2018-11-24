/*eslint no-console: "off"*/

const readline = require("readline");
const output = console.log.bind(console);
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
  const text = lines[0].trim();
  const counter = range(text.length / 3);
  const final = counter.reduce((count, index) => {
    return (
      count +
      ["P", "E", "R"].reduce((total, char, idx) => {
        return total + Number(char !== text[index * 3 + idx]);
      }, 0)
    );
  }, 0);

  output(final);
});
