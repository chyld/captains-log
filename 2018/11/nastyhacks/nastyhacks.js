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
  const output = lines
    .slice(1)
    .map(advertise)
    .join("\n");

  console.log(output);
});

function advertise(line) {
  const [r, e, c] = line.split(" ").map(s => s * 1);
  const net = e - c;

  if (r > net) return "do not advertise";
  else if (net > r) return "advertise";
  else return "does not matter";
}
