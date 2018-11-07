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
  const nums = lines[0]
    .split(" ")
    .map(n => parseInt(n))
    .sort((a, b) => a - b);

  const chars = lines[1].split("");
  const lookup = {};
  const results = [];

  for (const i in nums) {
    const num = nums[i];
    const letter = String.fromCharCode(65 + i * 1);
    lookup[letter] = num;
  }

  for (const char of chars) {
    results.push(lookup[char]);
  }

  console.log(results.join(" "));
});
