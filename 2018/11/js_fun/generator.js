function* odds() {
  x = 1;
  while (true) {
    yield x;
    x += 2;
  }
}

for (o of odds()) {
  console.log("o:", o);
  if (o > 20) break;
}
