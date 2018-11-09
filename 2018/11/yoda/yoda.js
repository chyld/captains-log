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
  const [top, bot] = Array.from({ length: lines.length }).map((n, i) =>
    lines[i]
      .split("")
      .map(c => parseInt(c))
      .reverse()
  );

  const n = Math.max(top.length, bot.length);
  let one = [];
  let two = [];

  Array.from({ length: n }).forEach((_, i) => {
    const t = top[i] || 0;
    const b = bot[i] || 0;

    if (t > b) one.push(t);
    else if (b > t) two.push(b);
    else {
      one.push(t);
      two.push(b);
    }
  });

  one = parseInt(one.reverse().join(""));
  two = parseInt(two.reverse().join(""));

  one = isNaN(one) ? "YODA" : one;
  two = isNaN(two) ? "YODA" : two;

  console.log(`${one}\n${two}`);
});
