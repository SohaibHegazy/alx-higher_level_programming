#!/usr/bin/node
const Father = require('./5-square');

module.exports = class Square extends Father {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let line = null;
        for (let j = 0; j < this.width; j++) {
          if (line === null) {
            line = c;
          } else {
            line += c;
          }
        }
        console.log(line);
      }
    }
  }
};
