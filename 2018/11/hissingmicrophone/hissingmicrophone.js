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
  const count = [...lines[0].toLowerCase()].reduce(countS, 0);
  const response = count ? "hiss" : "no hiss";
  output(response);
});

function countS(count, curr, idx, chars) {
  const prev = chars[idx - 1];
  if (!prev) return count;
  if (count === 2) return count;
  if (curr === "s" && prev === "s") return 2;
  return 0;
}
