#!/usr/bin/node

const Square = require('./5-square');

module.exports = class Square extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof (c) === undefined) {
      for (let i = 0; i < this.size; i++) {
        const c = 'C';
        console.log(c.repeat(this.size));
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        const x = 'X';
        console.log(x.repeat(this.size));
      }
    }
  }
};
