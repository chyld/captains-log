const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const lines = [];

rl.on("line", line => {
  lines.push(line);
});

rl.on("close", () => {
  const [N, P] = lines[0].split(" ").map(c => parseInt(c));
  console.log(P);
});
