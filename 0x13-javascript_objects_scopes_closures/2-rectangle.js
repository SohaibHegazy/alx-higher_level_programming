#!/usr/bin/node
// an empty class Rectangle that defines a rectangle

module.exports = class Rectangle {
  if (width > 0 && height > 0) {
    constructor (w, h) {
      this.width = w;
      this.height = h;
    }
  }
};
