/*eslint no-console: "off"*/

const Container = function(val) {
  this.val = val;
};

Container.of = function(val) {
  return new Container(val);
};

Container.prototype.map = function(fn) {
  const val = fn(this.val);
  return Container.of(val);
};

const a = new Container(3);
const b = Container.of(5);
const c = Container.of(7)
  .map(x => x / 2)
  .map(x => x - 1)
  .map(x => x * 3);

console.log(a, b, c);
