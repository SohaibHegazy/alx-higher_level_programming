#!/usr/bin/node
// a script that prints the addition of 2 integers

function add(a, b) {
    return a + b;
}

console.log(add(process.argv[2], process.argv[3]));