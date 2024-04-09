#!/usr/bin/node

exports.esrever = function (list) {
  let revList = [];
  for (let i = list.length, j = 0; i > 0; i--, j++) {
    revList[j] = list[i - 1];
  }
  return revList;
};
