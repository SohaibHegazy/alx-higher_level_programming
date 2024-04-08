#!/usr/bin/node
// searches the second biggest integer in the list of arguments

let max = 0;
let second_max = 0;

if (!process.argv[3]) {
  console.log(1);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > max) {
      second_max = max;
      max = parseInt(process.argv[i]);
    }
  }
  console.log(second_max);
}
