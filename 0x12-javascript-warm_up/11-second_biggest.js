#!/usr/bin/node
// searches the second biggest integer in the list of arguments

if (!process.argv[3]) {
  console.log(0);
} else {
  const argList = process.argv.sort();
  console.log(argList.reverse()[1]);
}
