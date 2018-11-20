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
  const db = getDb();
  const [, dom] = lines[0].trim().split(" ");
  const output = lines
    .slice(1)
    .map(line => db[line[0]][Number(line[1] !== dom)])
    .reduce((a, b) => a + b);

  console.log(output);
});

function getDb() {
  const db = {};
  const text = `
      A,11,11
      K,4,4
      Q,3,3
      J,20,2
      T,10,10
      9,14,0
      8,0,0
      7,0,0
  `;
  const lines = text
    .split("\n")
    .map(s => s.trim())
    .slice(1, -1);

  for (const line of lines) {
    const [c, a, b] = line.split(",");
    db[c] = [parseInt(a), parseInt(b)];
  }

  return db;
}
