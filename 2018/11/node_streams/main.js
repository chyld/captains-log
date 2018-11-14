const fs = require('fs');
const through = require('through2');

// read from input file
// fs.createReadStream(process.argv[2])

// read from stdin
process.stdin
  .pipe(through(write))
  .pipe(process.stdout);

function write(buf, enc, next){
  next(null, buf.toString().toUpperCase());
}

