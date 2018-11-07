const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let X, Y, N;

rl.on("line", line => {
  [X, Y, N] = line.split(" ").map(c => parseInt(c));
});

rl.on("close", () => {
  for (let i = 1; i <= N; i++) {
    if ((i % X) + (i % Y) === 0) console.log("FizzBuzz");
    else if (i % X == 0) console.log("Fizz");
    else if (i % Y == 0) console.log("Buzz");
    else console.log(i);
  }
});
