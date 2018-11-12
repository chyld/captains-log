const demo1 = {
  name: "hello, world",
  data: [3, 5, 7],
  [Symbol.iterator]: function*() {
    yield "alpha";
    for (n of this.data) {
      yield n;
    }
    yield "omega";
  }
};

for (d of demo1) {
  console.log("d:", d);
}

console.log("demo1:", [...demo1]);
