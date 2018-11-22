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
  const [h, v] = lines[0].split(" ").map(s => parseInt(s));
  const radian = v * (Math.PI / 180);
  const length = h / Math.sin(radian);
  const output = Math.ceil(length);
  console.log(output);
});
