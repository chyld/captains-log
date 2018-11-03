const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N = 0;

rl.on("line", line => {
  N = parseInt(line);
});

rl.on("close", () => {
  const result = Array.from({ length: N }, (x, i) => i + 1).map(
    i => `${i} Abracadabra`
  );
  const output = result.join("\n");
  console.log(output);
});
