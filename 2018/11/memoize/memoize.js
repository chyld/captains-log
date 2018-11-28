/*eslint no-console: "off"*/

console.log("hello");

function memoize(fn) {
  const table = {};

  return arg => {
    console.log("tb:", table);
    const o = table[arg] || (table[arg] = fn(arg));
    console.log("ta:", table);
    return o;
  };
}

function factorial(n) {
  if (n == 0) return 1;
  return n * factorial(n - 1);
}

const ff1 = memoize(factorial);
console.log(5, ff1(5));

const ff2 = memoize(n => {
  if (n == 0) return 1;
  return n * ff2(n - 1);
});
console.log(5, ff2(5));
