const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const numbers = [];

rl.on("line", line => {
  numbers.push(parseInt(line));
});

rl.on("close", () => {
  const [x, y] = numbers;
  const quadrants = [[1, 3], [4, 2]];
  console.log(quadrants[(x * y < 0) * 1][(x < 0) * 1]);
});
