/*eslint no-console: "off"*/

const Maybe = function(val) {
  this.val = val;
};

Maybe.of = function(val) {
  return new Maybe(val);
};

Maybe.prototype.isNothing = function() {
  return this.val === null || this.val === undefined;
};

Maybe.prototype.map = function(fn) {
  return this.isNothing() ? Maybe.of(null) : Maybe.of(fn(this.val));
};

const a = Maybe.of(3);
const b = Maybe.of(5).map(x => x * 2);
const c = Maybe.of(null).map(x => x + 1);

console.log(a, b, c);
