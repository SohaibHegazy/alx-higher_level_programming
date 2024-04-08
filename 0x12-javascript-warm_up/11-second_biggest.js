#!/usr/bin/node
// searches the second biggest integer in the list of arguments

if (process.argv.length < 4) {
  console.log(0);
} else {
  const argList = process.argv.sort();
  console.log(argList.reverse()[1]);
}
