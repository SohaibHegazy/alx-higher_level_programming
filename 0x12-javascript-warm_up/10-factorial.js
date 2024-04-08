#!/usr/bin/node
// a script that computes and prints a factorial

function getFactorial (n) {
  if ((isNaN(n)) || 1 === n) {
    return 1;
  } else {
    return n * getFactorial(n - 1);
  }
}

console.log(getFactorial(parseInt(process.argv[2])));
