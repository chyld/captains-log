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
  const magnatude = lines
    .slice(1)
    .map(s => s.length)
    .join("\n");
  output(magnatude);
});
