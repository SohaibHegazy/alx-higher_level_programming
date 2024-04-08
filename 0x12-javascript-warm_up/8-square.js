#!/usr/bin/node
// a script that prints a square

let line;

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    line = null;
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      if (line === null) {
        line = 'X';
      } else {
        line += 'X';
      }
    }
    console.log(line);
  }
}
