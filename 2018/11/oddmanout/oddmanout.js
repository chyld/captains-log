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
  for (let i = 2; i < lines.length; i += 2) {
    const set = lines[i].split(" ").reduce((set, n) => {
      set.has(n) ? set.delete(n) : set.add(n);
      return set;
    }, new Set());

    const loop = `Case #${i / 2}:`;
    console.log(loop, [...set.keys()][0]);
  }
});
