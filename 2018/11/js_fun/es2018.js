// rest + destructuring
const [a1, ...rest1] = [1, 3, 5];
console.log("a1:", a1, "rest1:", rest1);

const { a2, ...rest2 } = { a2: 3, b2: 2, c2: 1 };
console.log("a2:", a2, "rest2:", rest2);

// spread
const d1 = [1, 2, 3, ...[4, 5, 6]];
console.log("d1:", d1);

const d2 = { a: 1, b: 2, c: 3, ...{ d: 4, e: 5, f: 6 } };
console.log("d2:", d2);

// ------------------------------------------------------------- //
function add(a, b, c) {
  return a + b + c;
}
const e1 = add(...[1, 2, 3]);
console.log("e1:", e1);
// ------------------------------------------------------------- //

// promise
function rollDieAsync() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const roll = Math.floor(Math.random() * 6) + 1;
      resolve(roll);
    }, 100);
  });
}

rollDieAsync().then(x => console.log("x:", x));

// async generator
async function* rollDiceAsync(n) {
  for (let i = 0; i < n; i++) {
    yield await rollDieAsync();
  }
}

// async function
async function main() {
  for await (const roll of rollDiceAsync(3)) {
    console.log("roll:", roll);
  }
}

main();
