#!/usr/bin/node

const square = require('./5-square');

module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let x;
    if (c === undefined) {
      x = 'X';
    } else {
      x = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(x.repeat(this.width));
    }
  }
};
