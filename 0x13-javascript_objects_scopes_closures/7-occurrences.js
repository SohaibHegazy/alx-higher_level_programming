#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    searchElement === list[i] ? count++ : count;
    return count;
  }
}
