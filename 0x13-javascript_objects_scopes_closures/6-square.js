#!/usr/bin/node
const Parent = require('./5-square');

module.exports = class Square extends Parent {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < parseInt(this.height); i++) {
        let line = null;
        for (let j = 0; j < parseInt(this.width); j++) {
          if (line === null) {
            line = 'c';
          } else {
            line += 'c';
          }
        }
        console.log(line);
      }
    }
  }
};
