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
  const products = lines.slice(1).map(splitProduct);
  const qaly = products.reduce((a, c) => a + c);
  console.log(qaly.toFixed(3));
});

function splitProduct(line) {
  const [q, y] = line.split(" ").map(c => parseFloat(c));
  return q * y;
}
