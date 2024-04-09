#!/usr/bin/node
// an empty class Rectangle that defines a rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < parseInt(this.height); i++) {
      let line = null;
      for (let j = 0; j < parseInt(this.width); j++) {
        if (line === null) {
          line = 'X';
        } else {
          line += 'X';
        }
      }
      console.log(line);
    }
  }
};
