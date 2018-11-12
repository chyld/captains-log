function makeCounter(initial) {
  let count = initial;
  return function() {
    count += 1;
    return count;
  };
}

const counters = [];

for (let i = 0; i < 5; i++) {
  counters.push(makeCounter(i));
}

for (c of counters) {
  console.log(c, "--", c());
}
