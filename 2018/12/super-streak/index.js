const x = 3;
const y = 2;
const z = [1, 2, 3, 4, 5];

const a = z.map(n => n ** 2).map(n => n + 100);
console.log(x, y, z, a);
