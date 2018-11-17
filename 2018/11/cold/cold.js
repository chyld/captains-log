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
  const ranks = lines[0]
    .trim()
    .split(" ")
    .map(hand => hand[0]);

  const counter = new Map();

  for (const rank of ranks) {
    counter.set(rank, counter.has(rank) ? counter.get(rank) + 1 : 1);
  }

  const largest = Math.max(...counter.values());
  console.log(largest);
});
